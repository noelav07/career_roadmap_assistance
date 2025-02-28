from flask import Flask, request, jsonify, render_template
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route("/")
def home():
    return render_template("index.html")  # Looks for templates/index.html

@app.route("/chat", methods=["POST"])
def chat():
    if not API_KEY:
        return jsonify({"error": "API Key not found"}), 500

    data = request.json
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", json=data, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get-api-key")
def get_api_key():
    if not API_KEY:
        return jsonify({"error": "API Key not found"}), 500
    return jsonify({"api_key": API_KEY})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8503, debug=True)
