import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# load API key from .env
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_google(query):
    if not SERPAPI_KEY:
        raise ValueError("SERPAPI_KEY not found. Check your .env file.")
    params = {
        "engine": "google",
        "q": query,
        "location": "South Africa",
        "google_domain": "google.co.za",
        "gl": "za",
        "hl": "en",
        "api_key": SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])
