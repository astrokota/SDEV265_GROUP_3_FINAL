from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_search_dishes_pad_thai():
    response = client.get("/api/dishes/search?query=pad")

    assert response.status_code == 200
    
    data = response.json()

    assert data["query"] == "pad"
    assert "Pad Thai" in data["results"]

def test_prevalence_pad_thai():
    response = client.get("/api/dishes/Pad%20Thai/prevalence")

    assert response.status_code == 200

    data = response.json()

    assert data["dish"] == "Pad Thai"
    assert data["recipe_count"] == 8
    assert "allergens" in data
    assert len(data["allergens"]) > 0

    allergen_names = [item["allergen"] for item in data["allergens"]]

    assert "Peanuts" in allergen_names
    assert "Tree Nuts" in allergen_names

def test_unknown_dish():
    response = client.get("/api/dishes/Fake%20Dish/prevalence")

    assert response.status_code == 200

    data = response.json()

    assert data["dish"] == "Fake Dish"
    assert data["recipe_count"] == 0
    assert data["allergens"] == []