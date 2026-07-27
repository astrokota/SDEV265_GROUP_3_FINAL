import { useSearchParams, Link } from "react-router-dom";
import AllergenCard from "../components/AllergenCard";
import CountryComparison from "../components/CountryComparison";
import AllergenPercentages from "../components/VisualizationBar";
import mockData from "../mockData";
import { getDishPrevalence } from "../services/api";
import { useEffect, useState } from "react";

function Results(){
    const [searchParams] = useSearchParams();
    const dish = searchParams.get("dish");

    const[loading, setLoading] = useState(true);
    const[data, setData] = useState(true);
    const[error, setError] = useState("");

    useEffect(()=> {
        async function loadData() {
                try{
                    setLoading(true);
                    setError("");
                    const result = await getDishPrevalence(dish);

                    setData(result);
                } catch(err) {
                        setError("Unable to connect, please try again.")
                    } finally {
                        setLoading(false);
                    }
                
            }
        if (dish){
            loadData();
        }

    }, [dish]);

    if(loading){
        return <h2 id="searching">Searching...</h2>
    }

    if(error){
        return <h2 id="error">{error}</h2>
    }

    if(data && data.recipe_count === 0){
        return <div className="empty-state">
            <h2>No dish found</h2>
            <p>We couldn't find any recipes that matched "{dish}"</p>
            <Link to="/">
                <button>Search Again</button>
            </Link>

        </div>
    }
    
    return(
    <div id= "results-card"> 
        <h1>Search Results</h1><br/>
        <AllergenCard data ={data}/> <br/>
        <AllergenPercentages allergens={data.allergens} />
        <CountryComparison countries={mockData.countries}/>
        <footer>
            <p><br/><br/><strong>Disclaimer</strong>: Results are only estimates. User discretion advised.</p>
        </footer>
    </div>
    
    );
}

export default Results;