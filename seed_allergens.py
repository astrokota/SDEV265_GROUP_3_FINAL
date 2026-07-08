from database import SessionLocal
from models import Allergen, AllergenKeyword

allergen_data = {
    "Peanuts": ["peanut", "peanuts", "groundnut"],
    "Tree Nuts": ["almond", "cashew", "walnut", "pecan", "pistachio", "hazelnut", "macadamia", "brazil nut"],
}

db = SessionLocal()

db.query(AllergenKeyword).delete()
db.query(Allergen).delete()
db.commit()

for allergen_name, keywords in allergen_data.items():
    allergen = Allergen(name=allergen_name)
    db.add(allergen)
    db.commit()

    for keyword in keywords:
        db.add(AllergenKeyword(allergen_id=allergen.id, keyword=keyword))

    db.commit()

print("Seed complete.")
db.close()

