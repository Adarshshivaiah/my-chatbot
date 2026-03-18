from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
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
    
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)