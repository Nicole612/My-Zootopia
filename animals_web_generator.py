import json
from tempfile import template


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def generate_animals_data(animals_data):
    html_animals_infos = ""
    for animal in animals_data:
        if animal.get('name'):
            html_animals_infos += f"Name: {animal['name']}\n"
        if animal['characteristics'].get('order'):
            html_animals_infos += f"Diet: {animal['characteristics']['order']}\n"
        if animal.get('locations'):
            html_animals_infos += f"Location: {animal['locations']}\n"
        if animal['characteristics'].get('type'):
            html_animals_infos += f"Type: {animal['characteristics']['type']}\n"
        html_animals_infos += "\n"
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



