from openai import OpenAI
client = OpenAI(api_key='')

# client.files.create(
#   file=open("generated_dataset.jsonl", "rb"),
#   purpose="fine-tune"
# )=

def test_fine_tuned_model(model_name, prompt):
    try:
        response = client.completions.create(
            model=model_name,
            prompt=prompt,
            max_tokens=300,  # Adjust based on your needs
            temperature=0.7,  # Adjust based on your needs
            top_p=1.0,        # Adjust based on your needs
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    # Replace with your fine-tuned model ID
    fine_tuned_model_id = 'ft:davinci-002:personal:2chapter:A0Q86Ic0'
    
    # Test prompts
    test_prompts = [
        "how much money they spend on the project?",
    ]
    
    for prompt in test_prompts:
        print(f"Prompt: {prompt}")
        result = test_fine_tuned_model(fine_tuned_model_id, prompt)
        print(f"Response: {result}\n")

if __name__ == "__main__":
    main()

# import openai

# # Set up your API key
# # openai.api_key = 'your-api-key-here'

# # Set your fine-tuned model ID
# model_id = 'ft-<your-model-id>'

# # Prepare your test prompt
# messages = [
#     {"role": "user", "content": "Your test input here"}
# ]

# # Call the fine-tuned model
# response = client.chat.completions.create(
#     model=model_id,
#     messages=messages
# )

# # Print the response from the assistant
# print(response['choices'][0]['message']['content'])
