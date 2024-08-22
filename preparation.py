# import fitz  # PyMuPDF
# import camelot
# import json
# import re

# def extract_text_from_pdf(pdf_path):
#     seen_lines = set()
#     text = ""
#     with fitz.open(pdf_path) as doc:
#         for page in doc:
#             page_text = page.get_text("text").splitlines()  # Get text line by line
#             for line in page_text:
#                 line = line.strip()
#                 if line and line not in seen_lines:
#                     text += line + " "
#                     seen_lines.add(line)
#     return text

# def clean_text(text):
#     cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
#     cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)  # Remove non-ASCII characters
#     return cleaned_text.strip()

# pdf_path = "book.pdf"
# extracted_text = extract_text_from_pdf(pdf_path)
# cleaned_text = clean_text(extracted_text)

# def extract_tables_from_pdf(pdf_path):
#     seen_tables = set()
#     tables = camelot.read_pdf(pdf_path, pages="all", flavor='stream')
#     unique_tables = []
#     for table in tables:
#         table_str = table.df.to_string()
#         if table_str not in seen_tables:
#             unique_tables.append(table.df)
#             seen_tables.add(table_str)
#     return unique_tables

# extracted_tables = extract_tables_from_pdf(pdf_path)

# def save_to_jsonl(text, tables, output_file):
#     with open(output_file, 'w') as f:
#         for table in tables:
#             entry = {
#                 "text": text,
#                 "table": table.to_dict()
#             }
#             f.write(json.dumps(entry) + "\n")

# output_file = "output.jsonl"
# save_to_jsonl(cleaned_text, extracted_tables, output_file)
import json

# Load your JSON data
def load_data(json_file):
    with open(json_file, 'r') as file:
        return [json.loads(line) for line in file]

# Convert table data to text format
def table_to_text(table):
    if not table or not table.get('rows'):
        return ""
    headers = table['headers']
    rows = table['rows']
    table_text = "Table:\n"
    table_text += " | ".join(headers) + "\n"
    table_text += "-" * (len(headers) * 20) + "\n"
    for row in rows:
        table_text += " | ".join(row) + "\n"
    return table_text

# Process and write data to JSONL file
def format_to_jsonl(data, output_file):
    with open(output_file, 'w') as f:
        for entry in data:
            # Convert table to text format
            table_text = table_to_text(entry.get('table'))
            # Combine text and table
            formatted_entry = {
                "text": f"{entry['text']}\n\n{table_text}".strip()
            }
            # Write JSON object to file
            f.write(json.dumps(formatted_entry) + '\n')

# File paths
input_file = 'data.json'
output_file = 'formatted_dataset.jsonl'

# Load, process, and save the data
data = load_data(input_file)
format_to_jsonl(data, output_file)

print(f"Formatted dataset has been saved to {output_file}")
