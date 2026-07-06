from sqlalchemy.orm import Session
from models import Allergen, AllergenKeyword


def detect_allergens(normalized_ingredient: str, db: Session) -> list:
    """
    Given a normalized ingredient string, returns a list of allergen
    names (e.g. ["Peanuts"]) whose keywords appear in the ingredient.
    """
    keywords = db.query(AllergenKeyword).all()

    matched_allergen_ids = set()

    for kw in keywords:
        if kw.keyword in normalized_ingredient:
            matched_allergen_ids.add(kw.allergen_id)
    
    matched_names = []

    for allergen_id in matched_allergen_ids:
        allergen = db.query(Allergen).filter(Allergen.id == allergen_id).first()
        if allergen:
            matched_names.append(allergen.name)

    return matched_names