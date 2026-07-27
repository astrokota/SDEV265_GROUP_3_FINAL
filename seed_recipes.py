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
    {"dish_name": "Pad Thai", "title": "Shrimp Pad Thai", "ingredients": ["rice noodles", "shrimp", "eggs", "bean sprouts", "crushed peanuts", "tamarind"]},
    {"dish_name": "Pad Thai", "title": "Chicken Pad Thai", "ingredients": ["rice noodles", "chicken breast", "eggs", "peanuts", "lime", "fish sauce"]},
    {"dish_name": "Pad Thai", "title": "Vegan Pad Thai", "ingredients": ["rice noodles", "tofu", "bean sprouts", "roasted peanuts", "tamarind", "scallions"]},
    {"dish_name": "Pad Thai", "title": "Spicy Pad Thai", "ingredients": ["rice noodles", "shrimp", "chili flakes", "peanut butter", "eggs", "garlic"]},
    {"dish_name": "Pad Thai", "title": "Easy Weeknight Pad Thai", "ingredients": ["rice noodles", "eggs", "carrots", "cashews", "soy sauce", "lime"]},
    {"dish_name": "Almond Cake", "title": "Lemon Almond Cake", "ingredients": ["almond flour", "eggs", "sugar", "lemon zest", "butter"]},
    {"dish_name": "Almond Cake", "title": "Orange Almond Cake", "ingredients": ["ground almonds", "oranges", "eggs", "sugar", "baking powder"]},
    {"dish_name": "Almond Cake", "title": "Classic Almond Sponge", "ingredients": ["flour", "almond extract", "sliced almonds", "eggs", "butter", "sugar"]},
    {"dish_name": "Green Salad", "title": "Crunchy Green Salad", "ingredients": ["romaine lettuce", "cucumber", "walnuts", "olive oil", "lemon juice"]},
    {"dish_name": "Green Salad", "title": "Everyday House Salad", "ingredients": ["mixed greens", "tomatoes", "red onion", "vinaigrette"]},
    {"dish_name": "Green Salad", "title": "Spinach Avocado Salad", "ingredients": ["spinach", "avocado", "sunflower seeds", "olive oil", "lime juice"]},
    {"dish_name": "Brownies", "title": "Classic Fudge Brownies", "ingredients": ["flour", "cocoa powder", "butter", "eggs", "sugar", "vanilla"]},
    {"dish_name": "Brownies", "title": "Walnut Brownies", "ingredients": ["flour", "cocoa powder", "walnuts", "butter", "eggs", "sugar"]},
    {"dish_name": "Brownies", "title": "Peanut Butter Swirl Brownies", "ingredients": ["flour", "cocoa powder", "peanut butter", "eggs", "butter", "sugar"]},
    {"dish_name": "Brownies", "title": "Double Chocolate Brownies", "ingredients": ["flour", "cocoa powder", "chocolate chips", "butter", "eggs", "sugar"]},
    {"dish_name": "Brownies", "title": "Hazelnut Brownies", "ingredients": ["flour", "cocoa powder", "hazelnuts", "chocolate", "eggs", "butter"]},
    {"dish_name": "Chicken Satay", "title": "Grilled Chicken Satay", "ingredients": ["chicken thighs", "peanut sauce", "coconut milk", "soy sauce", "garlic"]},
    {"dish_name": "Chicken Satay", "title": "Thai Chicken Satay Skewers", "ingredients": ["chicken breast", "peanut butter", "curry powder", "coconut milk", "lime"]},
    {"dish_name": "Chicken Satay", "title": "Easy Chicken Satay", "ingredients": ["chicken", "crushed peanuts", "soy sauce", "brown sugar", "ginger"]},
    {"dish_name": "Chicken Satay", "title": "Almond Chicken Satay", "ingredients": ["chicken breast", "almond butter", "coconut milk", "lime", "garlic"]},
    {"dish_name": "Chicken Satay", "title": "Nut-Free Chicken Satay", "ingredients": ["chicken thighs", "sunflower seed butter", "soy sauce", "coconut milk", "ginger"]},
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

