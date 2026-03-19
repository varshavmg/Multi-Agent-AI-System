ffrom fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.controller import run_system

app = FastAPI(
    title="Multi-Agent AI System",
    description="Planner → Writer → Critic AI pipeline using Ollama",
    version="1.0"
)

class Request(BaseModel):
    topic: str


@app.get("/")
def home():
    return {"message": "Multi-Agent AI System is running 🚀"}


@app.post("/research")
def research(req: Request):
    result = run_system(req.topic)
    return result