from fastapi import FastAPI
from orchestrator import Orchestrator

app = FastAPI()
orc = Orchestrator()

@app.post("/run")
def run(repo_path: str):
    return {"result": orc.run(repo_path)}
