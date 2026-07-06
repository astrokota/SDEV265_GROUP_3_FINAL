from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    dish_name = Column(String)
    title = Column(String)
    source_name = Column(String)
    source_url = Column(String)
    region = Column(String)
    ingredients_text = Column(String)

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    raw_ingredient = Column(String)
    normalized_ingredient = Column(String)

class Allergen(Base):
    __tablename__ = "allergens"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class AllergenKeyword(Base):
    __tablename__ = "allergen_keywords"

    id = Column(Integer, primary_key=True)
    allergen_id = Column(Integer, ForeignKey("allergens.id"))
    keyword = Column(String)

class RecipeAllergenMatch(Base):
    __tablename__ = "recipe_allergen_matches"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    allergen_id = Column(Integer, ForeignKey("allergens.id"))
    matched_keyword = Column(String)

