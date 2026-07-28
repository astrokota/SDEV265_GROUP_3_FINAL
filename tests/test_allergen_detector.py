from database import SessionLocal
from services.ingredient_normalizer import normalize_ingredient
from services.allergen_detector import detect_allergens

def test_peanut_detection():
    db = SessionLocal()

    try:
        ingredient = normalize_ingredient("2 tbsp crushed peanuts")
        detected = detect_allergens(ingredient, db)

        assert "Peanuts" in detected

    finally:
        db.close()

def test_tree_nut_detection():
    db = SessionLocal()

    try:
        test_ingredients = [
            "1 cup almond flour",
            "chopped walnuts",
            "roasted cashews",
        ]

        for raw_ingredient in test_ingredients:
            ingredient = normalize_ingredient(raw_ingredient)
            detected = detect_allergens(ingredient, db)

            assert "Tree Nuts" in detected

    finally:
        db.close()

def test_nutmeg_not_false_positive():
    db = SessionLocal()

    try:
        ingredient = normalize_ingredient("1 tsp nutmeg")
        detected = detect_allergens(ingredient, db)

        assert "Peanuts" not in detected
        assert "Tree Nuts" not in detected

    finally:
        db.close()