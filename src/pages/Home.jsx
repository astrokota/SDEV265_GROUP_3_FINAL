import SearchBar from "../components/SearchBar";
function Home() {
    return (
        <div id="homepage">
            <h1>Global Allergen Search</h1><br/>
         {/*}  <img id="homeimg" src="/public/globe.png" alt=""></img> */}
            <p>A free online database dedicated to tracking allergen trends in dishes all around the world.</p> <br/>

            <SearchBar />
        </div>
    );
}

export default Home;