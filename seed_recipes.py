from database import SessionLocal
from models import Recipe, Ingredient

recipes_data = [
    {"dish_name": "Pad Thai", "title": "Classic Pad Thai", "ingredients": ["rice noodles", "2 tbsp crushed peanuts", "shrimp", "bean sprouts", "fish sauce"]},
    {"dish_name": "Pad Thai", "title": "Street-Style Pad Thai", "ingredients": ["rice noodles", "chopped peanuts", "tofu", "egg", "tamarind paste"]},
    {"dish_name": "Pad Thai", "title": "Peanut-Free Pad Thai", "ingredients": ["rice noodles", "chicken", "bean sprouts", "lime", "soy sauce"]},
    {"dish_name": "Almond Cake", "title": "Moist Almond Cake", "ingredients": ["1 cup ground almonds", "sugar", "eggs", "butter", "vanilla"]},
    {"dish_name": "Almond Cake", "title": "Flourless Almond Cake", "ingredients": ["2 cups almond flour", "honey", "eggs", "lemon zest"]},
    {"dish_name": "Green Salad", "title": "Garden Green Salad", "ingredients": ["lettuce", "cucumber", "tomato", "olive oil", "vinegar"]},
    {"dish_name": "Green Salad", "title": "Simple Side Salad", "ingredients": ["mixed greens", "carrot", "red onion", "lemon dressing"]},
]

db = SessionLocal()

db.query(Ingredient).delete()
db.query(Recipe).delete()
db.commit()

for recipe_info in recipes_data:
    recipe = Recipe(
        dish_name=recipe_info["dish_name"],
        title=recipe_info["title"],
    )
    db.add(recipe)
    db.commit()

    for raw in recipe_info["ingredients"]:
        db.add(Ingredient(recipe_id=recipe.id, raw_ingredient=raw))

    db.commit()

print("Recipes seeded.")
db.close()

