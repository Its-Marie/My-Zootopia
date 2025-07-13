import json

def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# Daten laden
animals_data = load_data("animals_data.json")

for animal in animals_data:
    if "name" in animal:
        print(f"Name: {animal['name']}")

    # "diet" kann entweder auf oberster Ebene oder unter "characteristics" liegen
    diet = animal.get("diet") or animal.get("characteristics", {}).get("diet")
    if diet:
        print(f"Diet: {diet}")

    # Erster Eintrag aus "locations", falls vorhanden
    if "locations" in animal and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")

    # "type" kann auch unter "characteristics" liegen
    type_ = animal.get("type") or animal.get("characteristics", {}).get("type")
    if type_:
        print(f"Type: {type_}")

    print()  # Leerzeile zwischen Tieren
