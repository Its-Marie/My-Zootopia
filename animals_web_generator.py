import json


def serialize_animal(animal):
    """Returns an HTML string for a single animal card."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    if "Diet" in animal and animal["Diet"]:
        output += f'    <strong>Diet:</strong> {animal["Diet"]}<br/>\n'
    if "Location" in animal and animal["Location"]:
        output += f'    <strong>Location:</strong> {animal["Location"]}<br/>\n'
    if "Type" in animal and animal["Type"]:
        output += f'    <strong>Type:</strong> {animal["Type"]}<br/>\n'

    output += '  </p>\n</li>\n'
    return output


def main():
    # 1. Read JSON file
    with open("animals.json", encoding="utf-8") as file:
        data = json.load(file)

    # 2. Generate HTML for all animals
    output = ""
    for animal in data:
        output += serialize_animal(animal)

    # 3. Read HTML template
    with open("animals_template.html", encoding="utf-8") as template_file:
        template = template_file.read()

    # 4. Replace placeholder with generated animal HTML
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Write final HTML to output file
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

    print("animals.html has been created!")


if __name__ == "__main__":
    main()
