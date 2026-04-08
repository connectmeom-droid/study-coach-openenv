from env.environment import StudyEnv

def run_task(task_id):
    env = StudyEnv()

    print("[START]")
    print(f"task_id: {task_id}")

    state = env.reset(task_id)

    # Simple baseline action
    action = {
        "Physics": 3,
        "Math": 2,
        "Chemistry": 1
    }

    state, reward, done, _ = env.step(action)

    print("\n[STEP]")
    print(f"action: {action}")
    print(f"reward: {reward}")

    print("\n[END]")
    print(f"final_score: {reward}")


if __name__ == "__main__":
    for task_id in [1, 2, 3]:
        run_task(task_id)