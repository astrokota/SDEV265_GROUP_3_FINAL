from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.dishes import router as dishes_router

app = FastAPI(title="Allergen Risk Analyzer API")
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

app.include_router(dishes_router)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
