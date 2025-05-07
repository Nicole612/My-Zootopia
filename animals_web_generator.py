import json
from tempfile import template


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def generate_animals_data(animals_data):
    html_animals_infos = ""
    for animal in animals_data:
        html_animals_infos += "<li class='cards__item'>"
        if animal.get("name"):
            animal_name = animal["name"]
            html_animals_infos += f"<div class='card__title'>{animal_name}</div>"
        html_animals_infos += "<p class='card__text'>"
        if animal["characteristics"].get("diet"):
            animal_diet = animal["characteristics"]["diet"]
            html_animals_infos += f"    <strong>Diet: </strong>{animal_diet}<br>"
        if animal.get("locations"):
            animal_locations = animal["locations"][0]
            html_animals_infos += f"    <strong>Location: </strong>{animal_locations}<br>\n"
        if animal["characteristics"].get("type"):
            animal_type = animal["characteristics"]["type"]
            html_animals_infos += f"    <strong>Type: </strong>{animal_type}<br>"
        html_animals_infos += "</p>"
        html_animals_infos += "<li>"
    return html_animals_infos

def main():
    animals_data = load_data('animals_data.json')
    with open("animals_template.html", "r") as file:
        template_html = file.read()
    updated_html_file = template_html.replace("__REPLACE_ANIMALS_INFO__", generate_animals_data(animals_data) )
    with open("animals.html", "w") as f:
        f.write(updated_html_file)

if __name__ == "__main__":
    main()



