responses = {
    "hi": "Hello! 👋 How can I help you?",
    "hello": "Hey there! Nice to meet you!",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I'm PyBot 2.0!",
    "what can you do": "I can chat with you and answer basic questions!",
    "bye": "Goodbye! Have a great day! 😊",
    "thanks": "You're welcome! 😄",
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm not sure about that. Can you rephrase?"

def chatbot():
    print("🤖 PyBot 2.0 is ready! Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Bot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

chatbot()