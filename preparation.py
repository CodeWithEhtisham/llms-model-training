import fitz  # PyMuPDF
import camelot
import json
import re

def extract_text_from_pdf(pdf_path):
    seen_lines = set()
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            page_text = page.get_text("text").splitlines()  # Get text line by line
            for line in page_text:
                line = line.strip()
                if line and line not in seen_lines:
                    text += line + " "
                    seen_lines.add(line)
    return text

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)  # Remove non-ASCII characters
    return cleaned_text.strip()

pdf_path = "book.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(extracted_text)

def extract_tables_from_pdf(pdf_path):
    seen_tables = set()
    tables = camelot.read_pdf(pdf_path, pages="all", flavor='stream')
    unique_tables = []
    for table in tables:
        table_str = table.df.to_string()
        if table_str not in seen_tables:
            unique_tables.append(table.df)
            seen_tables.add(table_str)
    return unique_tables

extracted_tables = extract_tables_from_pdf(pdf_path)

def save_to_jsonl(text, tables, output_file):
    with open(output_file, 'w') as f:
        for table in tables:
            entry = {
                "text": text,
                "table": table.to_dict()
            }
            f.write(json.dumps(entry) + "\n")

output_file = "output.jsonl"
save_to_jsonl(cleaned_text, extracted_tables, output_file)
