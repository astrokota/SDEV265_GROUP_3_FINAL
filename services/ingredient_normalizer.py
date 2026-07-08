import re

"""
Normalizes raw ingredient text into a clean, standardized form
for allergen keyword matching.
"""


def normalize_ingredient(raw_ingredient: str) -> str:
    """
    Takes a raw ingredient string (e.g. "2 cups chopped roasted peanuts")
    and returns a cleaned, lowercase, standardized version
    (e.g. "roasted peanuts") suitable for allergen keyword matching.
    """
    cleaned = raw_ingredient.lower().strip()
    cleaned = " ".join(cleaned.split())
    cleaned = re.sub(r"\d+/\d+", "", cleaned)
    cleaned = re.sub(r"\d+", "", cleaned)
    units = ["cups", "cup", "tbsp", "tsp", "oz", "ounces", "ounce", "g", "kg", "ml", "l", "lb", "lbs", "cloves", "clove", "pinch", "slices", "slice"]
    pattern = r"\b(" + "|".join(units) + r")\b"
    cleaned = re.sub(pattern, "", cleaned)
    prep_words = ["chopped", "diced", "minced", "sliced", "shredded", "grated", "crushed", "fresh", "freshly", "finely", "roughly", "thinly", "large", "small", "medium", "optional", "for garnish", "peeled"]
    prep_pattern = r"\b(" + "|".join(prep_words) + r")\b"
    cleaned = re.sub(prep_pattern, "", cleaned)
    cleaned = re.sub(r"[^\w\s]", "", cleaned)
    cleaned = " ".join(cleaned.split())


    return cleaned

