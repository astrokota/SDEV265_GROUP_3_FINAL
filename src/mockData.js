const mockData ={
    dish: "Pad Thai",
    recipe_count: 50,
    allergens: [
        {
            allergen: "Peanuts",
            prevalence: 88,
            matched_recipes: 30
        },
        {
            allergen: "Dairy",
            prevalence: 0,
            matched_recipes: 0
        },
        {
            allergen: "Eggs",
            prevalence: 61,
            matched_recipes: 28
        },
        {
            allergen: "Soy",
            prevalence: 90,
            matched_recipes: 30
        },
        {
            allergen: "Wheat",
            prevalence: 95,
            matched_recipes: 45
        },
        {
            allergen: "Shellfish",
            prevalence: 90,
            matched_recipes: 41
        },
    ],
    countries: [
        {
            country: "USA",
            risk: "Medium"
        },
        {
            country: "UK",
            risk: "Medium"
        },
        {
            country: "Thailand",
            risk: "High"
        }

    ]
};

export default mockData;