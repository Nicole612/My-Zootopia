import requests
import json
from tempfile import template


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animal(animal):
    """Generates HTML for a single animal as a <li> element"""
    animal_data = "<li class='cards__item'>"
    if animal.get("name"):
        animal_data += f"<div class='card__title'>{animal["name"]}</div>"
    animal_data += "<p class='card__text'>"
    if animal["characteristics"].get("diet"):
        animal_data += f"    <strong>Diet: </strong>{animal["characteristics"]["diet"]}<br>"
    if animal.get("locations"):
        animal_data += f"    <strong>Location: </strong>{animal["locations"][0]}<br>\n"
    if animal["characteristics"].get("type"):
        animal_data += f"    <strong>Type: </strong>{animal["characteristics"]["type"]}<br>"
    animal_data += "</p>"
    animal_data += "</li>"
    return animal_data


def generate_animals_data(animals_data):
    """ Generates the complete HTML string for a list of animals."""
    html_animals_infos = ""
    for animal in animals_data:
        html_animals_infos += serialize_animal(animal)
    return html_animals_infos

def main():
    API_KEY = "0mRBFkXQco3Snim/4O343Q==qRv3QTRm0jPEkVg6"
    res = requests.get(f"https://api.api-ninjas.com/v1/animals?name=Fox", headers={"X-Api-Key": API_KEY})
    animals_data = res.json()
    with open("animals_template.html", "r") as file:
        template_html = file.read()
    updated_html_file = template_html.replace("__REPLACE_ANIMALS_INFO__", generate_animals_data(animals_data) )
    with open("animals.html", "w") as f:
        f.write(updated_html_file)

if __name__ == "__main__":
    main()



