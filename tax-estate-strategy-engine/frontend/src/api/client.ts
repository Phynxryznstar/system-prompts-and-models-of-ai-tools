import axios from "axios";

// Points at the FastAPI backend (api/server.py). Override with a
// VITE_API_BASE_URL env var (e.g. in a .env file) if it runs elsewhere.
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});
