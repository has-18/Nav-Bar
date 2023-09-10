import openai
import time

# Set your OpenAI API key here
openai.api_key = "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"

# Generate a timestamp for the filename
timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
filename = timestamp + ".txt"

# Initialize the discussions with a system message
discussions = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Main loop for chatting
while True:
    user_input = input("You: ")  # User input
    if user_input.lower() == "quit":
        break

    # Add user input to discussions
    discussions.append({"role": "user", "content": user_input})

    # Create a chat completion
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=discussions
    )

    response = completion.choices[0].message.content
    print("AI:", response)

    # Add AI response to discussions
    discussions.append({"role": "assistant", "content": response})

    # Write the conversation to the log file
    with open(filename, 'a') as f:
        f.write("You: " + user_input + "\n")
        f.write("AI: " + response + "\n")

print("Have a nice day!")
