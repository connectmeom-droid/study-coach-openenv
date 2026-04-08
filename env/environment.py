from env.tasks import get_easy_task, get_medium_task, get_hard_task
import random


class StudyEnv:
    def __init__(self):
        self.current_task = None
        self.state_data = None

    def reset(self, task_id=1):
        if task_id == 1:
            self.current_task = get_easy_task()
        elif task_id == 2:
            self.current_task = get_medium_task()
        elif task_id == 3:
            self.current_task = get_hard_task()
        else:
            raise ValueError("Invalid task_id")

        self.state_data = {
            "hours_available": random.randint(4, 10),
            "weak_subject": random.choice(["Physics", "Math", "Chemistry"])
        }

        if task_id == 2:
            self.state_data["previous_score"] = round(random.uniform(0.3, 0.7), 2)

        if task_id == 3:
            self.state_data["history"] = [
                round(random.uniform(0.3, 0.7), 2) for _ in range(3)
            ]

        return self.state_data

    def step(self, action):
        try:
            reward = 0.2  # base reward (never zero)

            total_hours = sum(action.values())

            # ✅ Check total hours match
            if total_hours == self.state_data["hours_available"]:
                reward += 0.3

            # ✅ Check weak subject priority
            weak = self.state_data["weak_subject"]
            if action.get(weak, 0) >= 2:
                reward += 0.3

            # ✅ Extra logic for harder tasks
            if self.current_task["task_id"] == 2:
                if self.state_data.get("previous_score", 1) < 0.5:
                    if action.get(weak, 0) >= 3:
                        reward += 0.1

            if self.current_task["task_id"] == 3:
                history = self.state_data.get("history", [])
                if len(history) > 0 and sum(history)/len(history) < 0.6:
                    reward += 0.1

            # 🔥 FINAL STRICT CLAMP (ABSOLUTE GUARANTEE)
            reward = float(reward)

            if reward <= 0:
                reward = 0.01
            elif reward >= 1:
                reward = 0.99

            # prevent float edge cases
            if reward >= 0.999:
                reward = 0.99
            if reward <= 0.001:
                reward = 0.01

        except Exception as e:
            print("STEP ERROR:", str(e))
            reward = 0.5

        done = True
        print("FINAL REWARD SENT:", reward)
        return self.state_data, reward, done, {}

    def state(self):
        return self.state_data
    
