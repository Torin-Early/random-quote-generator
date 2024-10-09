import os
import json

# Path to the folder containing the quote files
quotes_folder = r'C:\Users\14137\PycharmProjects\random_quote_generator\quotes'

# Initialize an empty list to store the quotes
all_quotes = []

# Check if the folder exists and has files
if not os.path.exists(quotes_folder):
    print("The folder does not exist!")
else:
    # Loop through each file in the quotes folder
    for filename in os.listdir(quotes_folder):
        if filename.endswith('.txt'):  # Only process .txt files
            philosopher_name = filename.replace('.txt', '')  # Extract philosopher name from the filename
            print(f"Processing file: {filename}")  # Debugging print to see which files are being processed

            # Open and read the file
            file_path = os.path.join(quotes_folder, filename)
            print(f"Reading from {file_path}")  # Debugging to ensure file path is correct
            
            with open(file_path, 'r', encoding='utf-8') as file:
                quotes = file.readlines()  # Read all lines from the file
                if not quotes:
                    print(f"Warning: {filename} is empty.")  # Check if the file is empty
                else:
                    print(f"Found {len(quotes)} quotes in {filename}.")  # Show how many lines are read
                for quote in quotes:
                    quote = quote.strip()  # Remove any extra whitespace or newlines
                    if quote:  # Only add non-empty quotes
                        print(f"Adding quote: {quote}")  # Debugging print to check if quotes are being added
                        all_quotes.append({
                            'quote': quote,
                            'author': philosopher_name
                        })

# Check how many quotes were added
print(f"Total quotes extracted: {len(all_quotes)}")

# Output the collected quotes to a JSON file if quotes were found
if all_quotes:
    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_quotes, json_file, ensure_ascii=False, indent=4)
    print(f'Extracted {len(all_quotes)} quotes from {len(os.listdir(quotes_folder))} files.')
else:
    print("No quotes were extracted.")
