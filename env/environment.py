from env.tasks import get_easy_task, get_medium_task, get_hard_task
from env.graders import grade_easy, grade_medium, grade_hard
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

        # 🔥 UPGRADE: Dynamic + Personalized State
        self.state_data = {
            "hours_available": random.randint(4, 10),
            "weak_subject": random.choice(["Physics", "Math", "Chemistry"])
        }

        # Add extra fields for harder tasks
        if task_id == 2:
            self.state_data["previous_score"] = round(random.uniform(0.3, 0.7), 2)

        if task_id == 3:
            self.state_data["history"] = [
                round(random.uniform(0.3, 0.7), 2) for _ in range(3)
            ]

        return self.state_data

    def step(self, action):
        reward = 0.0

        if self.current_task["task_id"] == 1:
            reward = grade_easy(self.state_data, action)

        elif self.current_task["task_id"] == 2:
            reward = grade_medium(self.state_data, action)

        elif self.current_task["task_id"] == 3:
            reward = grade_hard(self.state_data, action)

        done = True

        return self.state_data, reward, done, {}

    def state(self):
        return self.state_data