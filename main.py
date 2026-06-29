from fastapi import FastAPI
app = FastAPI(title="Allergen Risk Analyzer API")

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

