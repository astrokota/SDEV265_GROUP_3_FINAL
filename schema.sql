CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    dish_name TEXT,
    title TEXT,
    source_name TEXT,
    source_url TEXT,
    region TEXT,
    ingredients_text TEXT
);

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER,
    raw_ingredient TEXT,
    normalized_ingredient TEXT
);

CREATE TABLE allergens (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE allergen_keywords (
    id INTEGER PRIMARY KEY,
    allergen_id INTEGER,
    keyword TEXT
);

CREATE TABLE recipe_allergen_matches (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER,
    allergen_id INTEGER,
    matched_keyword TEXT
);

