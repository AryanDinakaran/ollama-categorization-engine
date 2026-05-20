import ollama

model = "llama3.2:3b"

input_file = "data/datasheet.txt"
output_file = "data/categorised_datasheet.txt"

with open(input_file, "r") as f:
    items = f.read().strip()

prompt = f"""
    You are an assistant that categorizes and sorts grocery items.

    Here is a list of items:
    {items}

    I want you to:
    1. Categorize the items into the following categories: Fruits, Vegetables, Dairy, Meat, Grains, Beverages, Snacks, Household Items.
    2. Sort the items within each category alphabetically.
    3. Output the categorized and sorted list in a clear and organized format, with each category as a header followed by the items in that category.
"""

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_txt = response.get("response", "").strip()

    with open(output_file, "w") as f:
        f.write(generated_txt)

        print("Categorization and sorting complete. Output saved to:", output_file)

except Exception as e:
    print("An error occurred:", str(e))
