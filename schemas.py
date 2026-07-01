from pydantic import BaseModel

from typing import List


class AllergenResult(BaseModel):
    allergen: str
    prevalence: int
    matched_recipes: int


class DishPrevalenceResponse(BaseModel):
    dish: str
    recipe_count: int
    allergens: List[AllergenResult]