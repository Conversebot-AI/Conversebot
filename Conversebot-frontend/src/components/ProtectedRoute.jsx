import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode"; 
import api from "../api"; 
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"; 
import { useState, useEffect } from "react"; 

function ProtectedRoute({ children }) {
  // State to track if the user is authorized
  const [isAuthorized, setIsAuthorized] = useState(null);

  // Check authorization when the component loads
  useEffect(() => {
    auth().catch(() => setIsAuthorized(false)); // If auth fails, set authorization to false
  }, []);

  // Function to refresh the access token using the refresh token
  const refreshToken = async () => {
    const refreshToken = localStorage.getItem(REFRESH_TOKEN); // Get refresh token from localStorage
    try {
      // Call the API to refresh the token
      const res = await api.post("/api/token/refresh/", {
        refresh: refreshToken,
      });
      if (res.status === 200) {
        // If successful, update the access token and set authorized
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        setIsAuthorized(true);
      } else {
        // else set authorized to false
        setIsAuthorized(false);
      }
    } catch (error) {
      console.log(error);
      setIsAuthorized(false);
    }
  };

  // Function to check the current authentication status
  const auth = async () => {
    const token = localStorage.getItem(ACCESS_TOKEN); // Get access token from localStorage
    if (!token) {
      // If no token exists, set authorized to false
      setIsAuthorized(false);
      return;
    }
    const decoded = jwtDecode(token); // Decode the token to check its expiration
    const tokenExpiration = decoded.exp;
    const now = Date.now() / 1000;

    if (tokenExpiration < now) {
      // If token has expired, attempt to refresh it
      await refreshToken();
    } else {
      // If token is still valid, set authorized to true
      setIsAuthorized(true);
    }
  };

  // Render loading state while checking authorization
  if (isAuthorized === null) {
    return <div>Loading...</div>;
  }

  // If authorized, render the child components; otherwise, redirect to login
  return isAuthorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;