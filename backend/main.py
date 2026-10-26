
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_repository

app = FastAPI(title="Codebase Intelligence Engine")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post('/analyze')
def analyze(payload: dict):
    return analyze_repository(payload['path'])
