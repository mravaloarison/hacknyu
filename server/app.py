import os

from google import genai
from flask import Flask, request, jsonify
from flask_cors import CORS

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return jsonify({"message":"Hello, World!"})

@app.route("/ping")
def ping():
    return jsonify({"message":"pong"})

@app.route("/generate-content", methods=["POST"])
def generate_content():
    data = request.get_json()
    web_content = data.get("data")

    # print(web_content)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=["", web_content]
        )
        print(response.text)
        return jsonify({"response": response.text})
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})