import axios from "axios";

const api = axios.create({
    baseURL: "https://localhost:8000/api"
});

export const searchDishes = async(query) =>{
    const response = await api.get("/dishes/search", {params: {query}});
    return response.data;

};

export const getDishPrevalence = async (dish) => {
    const response = await api.get(`/dishes/${encodeURIComponent(dish)}/prevalence`);
    return response.data;
};

export default api;