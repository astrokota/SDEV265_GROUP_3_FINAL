function CountryComparison({countries}){
    return(
    <div className="card" id="country-card">
        <h2>Allergen risk by country</h2>
        <table>
            <thead>
                <tr>
                    <th>Country</th>
                    <th>Risk</th>
                </tr>
            </thead>
            <tbody>
                {countries.map((item)=>(<tr key={item.country}><td>{item.country}</td> <td>{item.risk}</td></tr>))}
            </tbody>
        </table>

    </div>
    )
}

export default CountryComparison;