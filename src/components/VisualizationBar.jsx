function AllergenPercentages({ allergens }) {
  return (
    <div className="card" id="visual-card">
      <h2>Allergen Prevalence</h2>

      <div className="chart">
        {allergens.map((item) => (
          <div key={item.allergen} className="bar-container">

            <span className="percent">
              {item.prevalence}%
            </span>

            <div className="bar" style={{ height: `${item.prevalence * 2}px` }}></div>

            <span className="label">
              {item.allergen}
            </span>

          </div>
        ))}
      </div>
    </div>
  );
}

export default AllergenPercentages;