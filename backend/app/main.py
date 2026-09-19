from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import resume

app = FastAPI(title="AI Career Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router, prefix="/api/v1/resume", tags=["Resume"])

@app.get("/")
def read_root():
    return {"message": "Hello World from FastAPI Backend!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
