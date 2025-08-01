import data_fetcher


def serialize_animal(animal):
    """Returns an HTML string for a single animal card."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    # Check for different possible field names in the API response
    if "characteristics" in animal and animal["characteristics"]:
        chars = animal["characteristics"]
        if "diet" in chars and chars["diet"]:
            output += f'    <strong>Diet:</strong> {chars["diet"]}<br/>\n'
        if "habitat" in chars and chars["habitat"]:
            output += f'    <strong>Location:</strong> {chars["habitat"]}<br/>\n'
        if "type" in chars and chars["type"]:
            output += f'    <strong>Type:</strong> {chars["type"]}<br/>\n'

    # Fallback to direct fields (in case API structure is different)
    if "diet" in animal and animal["diet"]:
        output += f'    <strong>Diet:</strong> {animal["diet"]}<br/>\n'
    if "habitat" in animal and animal["habitat"]:
        output += f'    <strong>Location:</strong> {animal["habitat"]}<br/>\n'
    if "locations" in animal and animal["locations"]:
        output += f'    <strong>Location:</strong> {", ".join(animal["locations"])}<br/>\n'

    output += '  </p>\n</li>\n'
    return output


def generate_error_message(animal_name):
    """Generates HTML for when no animal is found."""
    return f'''
    <div style="text-align: center; margin: 50px; padding: 20px; background-color: #f8f9fa; border-radius: 10px; border-left: 5px solid #dc3545;">
        <h2 style="color: #dc3545; margin-bottom: 15px;">🦊 Oops!</h2>
        <p style="font-size: 18px; color: #6c757d;">The animal "<strong>{animal_name}</strong>" doesn't exist in our database.</p>
        <p style="color: #6c757d;">Please try searching for a different animal!</p>
        <p style="font-size: 14px; color: #adb5bd; margin-top: 20px;">
            <em>Suggestion: Try common animals like "Fox", "Lion", "Eagle", or "Dolphin"</em>
        </p>
    </div>
    '''


def main():
    # 1. Ask user for animal name
    while True:
        animal_name = input("Enter a name of an animal: ").strip()
        if animal_name:
            break
        print("Please enter a valid animal name.")

    # 2. Fetch animal data using the data fetcher module
    print(f"Searching for '{animal_name}'...")
    data = data_fetcher.fetch_data(animal_name)

    # 3. Generate HTML content
    if not data:
        # No animals found - generate error message
        output = generate_error_message(animal_name)
        print(f"No animals found for '{animal_name}'.")
    else:
        # Generate HTML for all animals found
        output = ""
        for animal in data:
            output += serialize_animal(animal)
        print(f"Found {len(data)} animal(s) for '{animal_name}'.")

    # 4. Read HTML template
    try:
        with open("animals_template.html", encoding="utf-8") as template_file:
            template = template_file.read()
    except FileNotFoundError:
        print("Error: animals_template.html file not found!")
        return
    except Exception as e:
        print(f"Error reading template file: {e}")
        return

    # 5. Replace placeholder with generated content (either animals or error message)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    # 6. Write final HTML to output file
    try:
        with open("animals.html", "w", encoding="utf-8") as output_file:
            output_file.write(final_html)
        print("Website was successfully generated to the file animals.html.")
    except Exception as e:
        print(f"Error writing output file: {e}")


if __name__ == "__main__":
    main()
