from fastapi import FastAPI
from env.environment import StudyEnv

app = FastAPI()
env = StudyEnv()


@app.get("/")
def root():
    return {"message": "Study Coach Environment Running"}


# 🔥 REQUIRED RESET ENDPOINT
@app.post("/reset")
def reset_env():
    state = env.reset(1)
    return {"state": state}


# 🔥 ADD STEP ENDPOINT (CRITICAL)
@app.post("/step")
def step_env(action: dict):
    state, reward, done, _ = env.step(action)

    # 🔥 FORCE SAFE RANGE HERE ALSO
    if reward <= 0:
        reward = 0.01
    elif reward >= 1:
        reward = 0.99

    return {
        "state": state,
        "reward": reward,
        "done": done
    }
