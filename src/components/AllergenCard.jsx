
function AllergenCard ({data})
{
    return(
    <div className="card" id="allergen-card">
        <h2>{data.dish}</h2>
        <h3>Based on {data.recipe_count} recipes analyzed</h3> <br/>
        <ul>
            {data.allergens.map((item) => (<li key={item.allergen}>
                <strong>{item.allergen}</strong><br/>
                <small>Found in {item.matched_recipes} recipes</small>
                </li>
            ))}
        </ul>

    </div>

    );
}

export default AllergenCard;