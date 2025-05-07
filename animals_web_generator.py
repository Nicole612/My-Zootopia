import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
for animal in animals_data:
    if animal.get('name'):
        print(f"Name: {animal['name']}")
    if animal['characteristics'].get('order'):
        print(f"Diet: {animal['characteristics']['order']}")
    if animal.get('locations'):
        print(f"Location: {animal['locations']}")
    if animal['characteristics'].get('type'):
        print(f"Type: {animal['characteristics']['type']}")
    print()



