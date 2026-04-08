from env.environment import StudyEnv
from openai import OpenAI
import os
import json

# Initialize LLM client (VERY IMPORTANT)
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def get_action_from_llm(state):
    prompt = f"""
You are an AI study planner.

Given this student state:
{state}

Generate a study plan in JSON format like:
{{
    "Physics": int,
    "Math": int,
    "Chemistry": int
}}

Total hours must match available time.
"""

    try:
        model_name = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        action = json.loads(output)

    except Exception as e:
        print("LLM ERROR:", str(e))

        # fallback action (VERY IMPORTANT)
        action = {
            "Physics": 3,
            "Math": 2,
            "Chemistry": 1
        }

    return action


def run_task(task_id):
    env = StudyEnv()

    print("[START]")
    print(f"task_id: {task_id}")

    state = env.reset(task_id)

    # 🔥 Use LLM here
    action = get_action_from_llm(state)

    state, reward, done, _ = env.step(action)

    print("\n[STEP]")
    print(f"action: {action}")
    print(f"reward: {reward}")

    print("\n[END]")
    print(f"final_score: {reward}")


if __name__ == "__main__":
    for task_id in [1, 2, 3]:
        run_task(task_id)
