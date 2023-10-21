import random

# Define a dictionary of predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm just a chatbot, but thanks for asking!", "I'm doing well, thank you!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm just a chatbot, and I'm not sure how to respond."],
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no match found, return a default response
    return random.choice(responses["default"])

# Main chat loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
