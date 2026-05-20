# Ollama Grocery List Categorizer

A dead-simple Python utility that uses a local Ollama LLM to automatically categorize and sort grocery items from a text file.

## Overview

This is a quick 5-minute coffee break project. It reads a plain text file containing a list of grocery items (one per line) and uses the `llama3.2:3b` model running locally via Ollama to categorize them into meaningful groups (Fruits, Vegetables, Dairy, Meat, Grains, Beverages, Snacks, Household Items) and sort them alphabetically within each category.

Perfect for testing out local LLMs with a practical use case!

## Requirements

- **Python 3.7+**
- **Ollama** installed and running locally
- **ollama Python package** for interacting with Ollama

## Installation

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull the required model:
   ```bash
   ollama pull llama3.2:3b
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your grocery list in `data/datasheet.txt` (one item per line)
2. Run the script:
   ```bash
   python main.py
   ```
3. The categorized output will be saved to `data/categorised_datasheet.txt`

## Example

**Input** (`data/datasheet.txt`):

```
apple
banana
carrot
spinach
tomato
milk
eggs
bread
```

**Output** (`data/categorised_datasheet.txt`):

```
Fruits
• Apple
• Banana

Vegetables
• Carrot
• Spinach
• Tomato

Dairy
• Eggs
• Milk

Grains
• Bread
```

## Project Structure

```
ollama-categorization-engine/
├── main.py                    # Main script
├── data/
│   ├── datasheet.txt         # Input grocery list
│   └── categorised_datasheet.txt  # Output (generated)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## How It Works

1. Reads items from `data/datasheet.txt`
2. Constructs a prompt with categorization instructions
3. Sends the prompt to the local Ollama model (`llama3.2:3b`)
4. Parses the response and writes the categorized list to `data/categorised_datasheet.txt`
5. Prints a completion message

## Notes

- Requires Ollama to be running: Start with `ollama serve`
- The model quality and categorization accuracy depend on the `llama3.2:3b` model
- Categories are: Fruits, Vegetables, Dairy, Meat, Grains, Beverages, Snacks, Household Items
- Items are sorted alphabetically within each category

## License

This project is open source and available under the MIT License.
