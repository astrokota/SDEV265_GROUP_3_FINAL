
function AllergenCard ({data})
{
    return(
    <div className="card" id="allergen-card">
        <h2>{data.
        dish}</h2>
        <h3>{data.recipe_count} recipes found</h3>
        <ul>
            {data.allergens.map((item) => (<li key={item.allergen}>
                <u>{item.allergen}</u><br/>
                Prevalence: {item.prevalence}% <br/>
                In {item.matched_recipes} recipes
                </li>
            ))}
        </ul>

    </div>

    );
}

export default AllergenCard;