import axios from "axios"; // Import axios for making HTTP requests
import { ACCESS_TOKEN } from "./constants"; 

// Create an axios instance with a base URL configured
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // Set the base URL for API requests from .env
});

// Add a request interceptor to include the authorization token in every request
api.interceptors.request.use(
  (config) => {
    // Retrieve the access token from localStorage
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      // If the token exists, add it to the Authorization header for the request
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config; // Return the modified config
  },
  (error) => {
    // Handle errors
    return Promise.reject(error); // Reject the promise with the error
  }
);

export default api;
