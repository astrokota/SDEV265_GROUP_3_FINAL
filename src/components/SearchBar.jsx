import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SearchBar() {
  const [dish, setDish] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!dish.trim()) return;

    navigate(`/results?dish=${encodeURIComponent(dish)}`);
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
      </form>
    </div>
  );
}

export default SearchBar;