import json

# 1. JSON-Datei lesen
with open("animals.json") as file:
    data = json.load(file)

# 2. Tierdaten als String generieren
output = ''
for animal in data:
    output += f"Name: {animal['name']}<br>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br>\n"
    output += f"Location: {animal['geography']['continents'][0]}<br>\n"
    output += f"Type: {animal['taxonomy']['class']}<br><br>\n"

# 3. HTML-Template lesen
with open("animals_template.html") as template_file:
    template = template_file.read()

# 4. Platzhalter ersetzen
final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Neue HTML-Datei schreiben
with open("animals.html", "w") as output_file:
    output_file.write(final_html)

print("animals.html wurde erstellt!")
