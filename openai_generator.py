from openai import OpenAI

client = OpenAI(api_key='')
import json

# Set up your OpenAI API key

# Set up your OpenAI API key


def generate_prompts_and_completions(paragraph):
    print(paragraph[:50])
    questions = []

    # Generate two questions based on the paragraph
    for _ in range(2):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that generates questions based on provided text."},
                {"role": "user", "content": f"Generate a question based on the following paragraph: {paragraph}"}
            ],
            max_tokens=50
        )
        question = response.choices[0].message.content
        questions.append(question)

        # After generating each question, print and save it immediately
        print(f"Generated question: {question}")

    # Prepare dataset entries with paragraph and questions
    entries = [{"prompt": question, "completion": paragraph.strip()} for question in questions]

    return entries

# Function to process text file and generate dataset
def process_text_file(file_path):
    # Read the text file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into paragraphs based on double newline
    paragraphs = content.split('\n\n')

    # Initialize a list to store the dataset entries
    dataset = []

    # Generate prompts and completions for each paragraph
    for paragraph in paragraphs:
        if paragraph.strip():  # Check if paragraph is not empty
            entries = generate_prompts_and_completions(paragraph)
            dataset.extend(entries)  # Add all entries (questions and paragraph pairs) to the dataset

            # Save the dataset to a JSONL file after processing each paragraph
            with open('generated_dataset.jsonl', 'w') as f:
                for entry in dataset:
                    json.dump(entry, f)
                    f.write('\n')

            print("Dataset has been updated and saved to 'generated_dataset.jsonl'.")

# Specify the path to your text file
text_file_path = 'formatted_output.txt'

# Call the function to process the text file and generate the dataset
process_text_file(text_file_path)