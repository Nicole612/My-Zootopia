import os
from dotenv import load_dotenv
import requests


load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_query):
    res = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_query}", headers={"X-Api-Key": API_KEY})
    if res.status_code == 200:
        return res.json()
    else:
        return []
