from openai import OpenAI
 
client = OpenAI(api_key="")
 

# Read the content of the file
file_path = 'test.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

# Make a request to the OpenAI API with the file content
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an assistant."},
        {"role": "user", "content": file_content}
    ]
)

# Print the response from the model
print(response['choices'][0])
