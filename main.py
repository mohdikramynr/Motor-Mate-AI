from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from tools.symptom_analyzer import symptom_analyzer
from agents.mechanic_agent import MechanicAgent

app = FastAPI(title="MotorMate API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    symptom: str
    model: str

@app.get("/")
def home():
    return {"message": "MotorMate API is running!"}

@app.post("/diagnose")
def diagnose(data: Query):
    triage = symptom_analyzer(data.symptom)
    mech = MechanicAgent({})
    steps = mech.generate_steps(triage[0][0], data.model)
    return {"triage": triage, "repair_steps": steps["steps"]}
