import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { searchDishes } from "../services/api";

function SearchBar() {
  const [dish, setDish] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!dish.trim()) return;
    try{
      const result = await searchDishes(dish);
      if(result.results.length === 0){
        setMessage("No matching dishes found.")
        return;
      }
      navigate(`/results?dish=${encodeURIComponent(result.results[0])}`);
    } catch (error){
      setMessage("Unable to connect to the server, please try again.");
    }
    
  };

  return (
    <div id="search-bar">
      <form onSubmit={handleSubmit}>
        <label htmlFor="search-key">
          What would you like to eat today?
        </label>

        <br/>

        <input type="search" id="search-key" value={dish} placeholder="Ex: pad thai, pesto sauce, brownies..." required
          onChange={(e) => setDish(e.target.value)}
        />

        <button type="submit" id="buttom" >Search</button>
      </form> <br/>
      {message && <p className="error-message">{message}</p>}
    </div>
  );
}

export default SearchBar;