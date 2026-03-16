from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    bot_reply = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": bot_reply
    })
    return bot_reply

def main():
    print("🤖 AI Chatbot powered by Groq! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye! 👋")
            break
        response = chat(user_input)
        print(f"Bot: {response}\n")

main()