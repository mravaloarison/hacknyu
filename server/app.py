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
    prompt = """
        Analyze this image and/or text for any inappropriate, harmful, or offensive elements. 
        Look for explicit content, violence, hate speech, threats, self-harm, illegal activity, misinformation, profanity, 
        and any graphic material. Provide a reason for your determination. 
        Additionally, analyze this text/image and determine if it is AI-generated. 
        Look for signs such as unnatural phrasing, repetitive structure, inconsistencies, visual artifacts, 
        or metadata indicating AI origin. Provide a confidence score and an explanation for your determination.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=[prompt, web_content]
        )
        print(response.text)
        return jsonify({"response": response.text})
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})