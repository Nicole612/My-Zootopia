import requests
import json
from animals_web_generator import generate_animals_data

API_KEY = "0mRBFkXQco3Snim/4O343Q==qRv3QTRm0jPEkVg6"

def fetch_data(animal_query):
    res = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_query}", headers={"X-Api-Key": API_KEY})
    if res.status_code == 200:
        return res.json()
    else:
        return []
