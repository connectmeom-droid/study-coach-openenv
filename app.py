from fastapi import FastAPI
import subprocess
from env.environment import StudyEnv

app = FastAPI()
env = StudyEnv()

@app.get("/")
def run_env():
    result = subprocess.run(["python", "inference.py"], capture_output=True, text=True)
    return {"output": result.stdout}

# 🔥 REQUIRED ENDPOINT
@app.get("/reset")
def reset_env():
    state = env.reset(1)
    return {"state": state}