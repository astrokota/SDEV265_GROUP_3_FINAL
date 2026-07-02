import { useSearchParams } from "react-router-dom";
import AllergenCard from "../components/AllergenCard";
import CountryComparison from "../components/CountryComparison";
import mockData from "../mockData";
import { useEffect, useState } from "react";

function Results(){
    const [searchParams] = useSearchParams();
    const dish = searchParams.get("dish");

    const[loading, setLoading] = useState(true);
    const[data, setData] = useState(null);
    const[error, setError] = useState("");

    useEffect(()=>{setLoading(true); setError("");
        setTimeout (()=>
        {
            if(dish && dish.toLowerCase() === mockData.dish.toLowerCase())
            {
                setData(mockData);
            } else{
                setData(null);
                setError("No results found.")
            }
            setLoading(false);
        },1000);
    }, [dish]);

    if(loading){
        return <h2 id="searching">Searching...</h2>
    }
    if(error){
        return <h2 id="error">{error}</h2>
    }    
    return(
    <div id= "results-card"> 
        <h1>Search Results</h1><br/>
        <AllergenCard data ={mockData}/> <br/>
        <CountryComparison countries={mockData.countries}/>
        <footer>
            <p><br/><br/><strong>Disclaimer</strong>: Results are only estimates. User discretion advised.</p>
        </footer>
    </div>
    
    );
}

export default Results;