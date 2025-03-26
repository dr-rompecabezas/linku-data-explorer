# lipu Linku Data Explorer

This utility fetches data from the [lipu Linku API](https://api.linku.la/v1/words), extracts core Toki Pona words, and saves their full data entries to a JSON file. It also verifies that all core words are accounted for in the exported data.

## Features

1. **Fetch Data**: Retrieves word data from the Linku API.
2. **Core Word Extraction**: Filters the data to include only core Toki Pona words, as defined in the `CORE_WORDS` list.
3. **Serialization**: Saves the full data entries of core words to a JSON file (`core_words.json`).
4. **Verification**: Ensures that every word in `CORE_WORDS` has a corresponding entry in the exported data.

## How to Use

1. Clone the repository and navigate to the project directory.
2. Ensure that the `constants.py` file contains the `CORE_WORDS` list, which defines the core Toki Pona words.
3. Run the script:

   ```bash
   python main.py
   ```

4. The script will:
   - Fetch data from the API.
   - Extract and save core word data to `core_words.json`.
   - Verify that all core words are included in the exported data.

## Output

- **core_words.json**: A JSON file containing the full data entries for all core Toki Pona words.

## Requirements

- Python 3.x
- `requests` library
- `uv` utility

Use uv to activate a virtual environment and install requirements:

```bash
uv sync
```

## Example

If the `CORE_WORDS` list contains `["a", "ike", "pona"]`, the script will:

- Fetch data from the API.
- Extract the full data entries for the words `"a"`, `"ike"`, and `"pona"`.
- Save these entries to `core_words.json`.
- Verify that all words in `CORE_WORDS` are included in the exported data.

## Notes

- Ensure that the API endpoint (`API_URL`) is accessible.
- Update the `CORE_WORDS` list in `constants.py` as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

The Linku API is provided by [lipu Linku](https://github.com/lipu-linku) and is subject to their terms and conditions.

As of the time of this commit, lipu Linku (linku.la) is licensed under the GNU General Public License Version 3.
