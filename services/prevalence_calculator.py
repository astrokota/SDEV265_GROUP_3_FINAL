from sqlalchemy.orm import Session
from models import Recipe, Ingredient
from services.ingredient_normalizer import normalize_ingredient
from services.allergen_detector import detect_allergens
from schemas import AllergenResult, DishPrevalenceResponse


def calculate_prevalence(dish_name: str, db: Session) -> DishPrevalenceResponse:
    """
    Given a dish name, finds all recipes for that dish, detects allergens
    in each, and returns a DishPrevalenceResponse with prevalence
    percentages per allergen.
    """
    recipes = db.query(Recipe).filter(Recipe.dish_name.ilike(dish_name)).all()
    recipe_count = len(recipes)

    if recipe_count == 0:
        return DishPrevalenceResponse(
            dish=dish_name,
            recipe_count=0,
            allergens=[],
        )

    allergen_counts = {}

    for recipe in recipes:
        ingredients = db.query(Ingredient).filter(Ingredient.recipe_id == recipe.id).all()

        found_allergens = set()

        for ingredient in ingredients:
            normalized = normalize_ingredient(ingredient.raw_ingredient)
            detected = detect_allergens(normalized, db)
            for allergen_name in detected:
                found_allergens.add(allergen_name)

        for allergen_name in found_allergens:
            allergen_counts[allergen_name] = allergen_counts.get(allergen_name, 0) + 1

    allergen_results = []

    for allergen_name, count in allergen_counts.items():
        prevalence = round((count / recipe_count) * 100)
        allergen_results.append(
            AllergenResult(
                allergen=allergen_name,
                prevalence=prevalence,
                matched_recipes=count,
            )
        )

    allergen_results.sort(key=lambda r: r.prevalence, reverse=True)

    return DishPrevalenceResponse(
        dish=dish_name,
        recipe_count=recipe_count,
        allergens=allergen_results,
    )