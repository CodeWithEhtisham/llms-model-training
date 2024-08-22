import json

# Function to convert the JSON structure to a readable text format
def convert_to_training_format(data):
    output = []
    
    # Loop through each dictionary in the JSON list
    for entry in data:
        # Add text field if available
        if "text" in entry:
            output.append(f"Text: {entry['text']}\n")
        
        # If there is a table, format the table content
        if "table" in entry and entry["table"]:
            table = entry["table"]
            output.append("Table:\n")
            
            # Add headers
            headers = table.get("headers", [])
            if headers:
                output.append(" | ".join(headers) + "\n")
                output.append("-" * (len(" | ".join(headers))) + "\n")
            
            # Add rows
            rows = table.get("rows", [])
            for row in rows:
                output.append(" | ".join(row) + "\n")
            output.append("\n")
    
    # Join all parts into a single string
    return "".join(output)

# Load the JSON data from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Save formatted data to a text file
def save_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)

# Example usage with a JSON file
json_file_path = 'data.json'  # Replace with your actual file path
output_file_path = 'formatted_output.txt'  # Output file path

# Load the JSON data
json_data = load_json(json_file_path)

# Convert the data
formatted_data = convert_to_training_format(json_data)

# Save the formatted data to a text file
save_to_file(formatted_data, output_file_path)

print(f"Data has been formatted and saved to {output_file_path}")
