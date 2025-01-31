import requests
import logging
from django.conf import settings

# Logger setup
logger = logging.getLogger(__name__)

URL_BASE = "https://api.spoonacular.com"

def fetch(endpoint, params=None):
    params = params or {}
    params["apiKey"] = settings.API_KEY  

    url = f"{URL_BASE}/{endpoint}"  
    try:
        logger.info(f"Fetching data from: {url} with params: {params}")

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() 
        return response.json()  
    except requests.exceptions.Timeout:
        logger.error(f"Timeout occurred while fetching {url}")
        return {"error": "Request timed out. Please try again."}

    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error while fetching {url}")
        return {"error": "Unable to connect to the server. Check your connection."}

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
        return {"error": f"HTTP Error {e.response.status_code}: {e.response.reason}"}

    except requests.exceptions.RequestException as e:
        logger.error(f"Unexpected error while fetching {url}: {e}")
        return {"error": str(e)}
