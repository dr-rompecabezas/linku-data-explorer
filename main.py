import json

import requests

from constants import CORE_WORDS

# API endpoint
API_URL = "https://api.linku.la/v1/words"


def fetch_data(url):
    """Fetches data from the given API URL and returns JSON."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def is_core_word(word):
    """Checks if a word is a core Toki Pona word."""
    return word in CORE_WORDS


def extract_core_words(data):
    """Extracts and returns core word dictionaries from the data."""
    if isinstance(data, dict):
        data = list(data.values())  # Convert dictionary values to a list

    if not isinstance(data, list):
        print("Unexpected data format. Unable to process.")
        return []

    return [entry for entry in data if is_core_word(entry.get("word", ""))]


def serialize_core_words(core_words, filename="core_words.json"):
    """Serializes core word dictionaries to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(core_words, file, indent=2, ensure_ascii=False)

    print(f"Core words saved to {filename}")


def verify_core_words(core_words):
    """Verifies that every word in CORE_WORDS has an entry in the core words data."""
    core_word_set = set(CORE_WORDS)
    exported_word_set = {entry.get("word", "") for entry in core_words}

    missing_words = core_word_set - exported_word_set
    if missing_words:
        print(f"Missing core words: {missing_words}")
    else:
        print("All core words are accounted for.")


if __name__ == "__main__":
    data = fetch_data(API_URL)
    if data:
        core_words = extract_core_words(data)
        serialize_core_words(core_words, filename="core_words.json")
        verify_core_words(core_words)
