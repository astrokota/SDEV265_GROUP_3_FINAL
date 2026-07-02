from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Recipe
from schemas import DishPrevalenceResponse
from services.prevalence_calculator import calculate_prevalence

router = APIRouter(prefix="/api/dishes", tags=["dishes"])

@router.get("/search")
def search_dishes(query: str, db: Session = Depends(get_db)):
    recipes = db.query(Recipe).filter(Recipe.dish_name.ilike(f"%{query}%")).all()
    dish_names = sorted(set(r.dish_name for r in recipes))
    return {"query": query, "results": dish_names}

@router.get("/{dish}/prevalence", response_model=DishPrevalenceResponse)
def dish_prevalence(dish: str, db: Session = Depends(get_db)):
    return calculate_prevalence(dish, db)

