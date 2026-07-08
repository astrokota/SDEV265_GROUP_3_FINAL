from fastapi import FastAPI
from api.dishes import router as dishes_router

app = FastAPI(title="Allergen Risk Analyzer API")
app.include_router(dishes_router)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
