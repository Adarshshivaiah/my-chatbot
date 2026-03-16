def chatbot():
    print("🤖 Hello! I'm your first chatbot. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "quit":
            print("Bot: Goodbye! 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How are you doing?")
        elif "how are you" in user_input:
            print("Bot: I'm just a bot, but I'm doing great! 😄")
        elif "your name" in user_input:
            print("Bot: My name is PyBot!")
        elif "weather" in user_input:
            print("Bot: I can't check weather yet, but it's always sunny in Python! ☀️")
        elif "bye" in user_input:
            print("Bot: Bye! Take care! 👋")
            break
        else:
            print("Bot: Hmm, I don't understand that yet. Try asking something else!")

# Run the chatbot
chatbot()

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