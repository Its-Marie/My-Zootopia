import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = f"{BASE_URL}?name={animal_name}"

    headers = {
        'X-Api-Key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error during API request: {response.status_code}")
            return []

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []
    except json.JSONDecodeError:
        print("Error parsing API response")
        return []