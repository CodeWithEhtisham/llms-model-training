import json

# Open the input and output files
with open('generated_dataset.jsonl', 'r') as infile, open('chat.jsonl', 'w') as outfile:
    for line in infile:
        # Load the JSON object from each line
        item = json.loads(line)

        # Convert to the chat format
        chat_item = {
            "messages": [
                {"role": "user", "content": item["prompt"]},
                {"role": "assistant", "content": item["completion"]}
            ]
        }

        # Write the new chat-formatted JSON object to the output file
        outfile.write(json.dumps(chat_item) + '\n')
