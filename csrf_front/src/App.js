import "./App.css";
import axios from "axios";
import { useEffect } from "react";
import Cookies from "universal-cookie";

function App() {
  useEffect(() => {
    const response = axios.get("http://127.0.0.1:8000/product/csrf/");
    console.log(response);
  }, []);

  const cookies = new Cookies();

  console.log(cookies.get("csrftoken"));

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    const response = await axios.post("http://127.0.0.1:8000/product/", data, {
      headers: {
        "content-type": "application/json",
        "Access-Control-Allow-Credentials": true,
        "Access-Control-Allow-Origin": "http://localhost:8000",
        // "Access-Control-Allow-Methods": ["POST"],
        "x-csrftoken": cookies.get("csrftoken"),
      },
      withCredentials: true,
      crossDomain: true,
    });
  };
  
  return (
    <div className="App">
      <form method="POST" onSubmit={handleSubmit} encType="multipart/form-data">
        <input
          type="text"
          placeholder="Enter your product name"
          name="product_name"
        />
        <input
          type="number"
          placeholder="Enter your product price"
          name="product_price"
        />
        <input
          type="number"
          placeholder="Enter your product quantity"
          name="product_quantity"
        />
        <input
          type="text"
          placeholder="Enter your product description"
          name="product_description"
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
