import json

# Open the input and output files
with open('version1.jsonl', 'r') as infile, open('version2.jsonl', 'w') as outfile:
    for line in infile:
        # Load the JSON object from each line
        item = json.loads(line)
        
        # Set the prompt to an empty string
        item["prompt"] = ""
        
        # Write the modified JSON object to the output file
        outfile.write(json.dumps(item) + '\n')
