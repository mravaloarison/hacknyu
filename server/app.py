import os, json

from google import genai
from google.genai import types
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import WebsiteAnalysis
from sp import SP
import urllib.request 
from PIL import Image 

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return jsonify({"message":"Hello, World!"})

@app.route("/ping")
def ping():
    return jsonify({"message":"pong"})

# @app.route("/generate-content", methods=["POST"])
# def generate_content():
#     data = request.get_json()
#     web_content = data.get("data")

#     image = requests.get(web_content)

#     try:
#         response = client.models.generate_content(
#             model= "gemini-2.0-flash-exp",
#             contents=[SP, types.Part.from_bytes(image.content, "image/jpeg")],
#             config={
#                 "response_mime_type": "application/json",
#                 "response_schema": WebsiteAnalysis,
#                 "temperature": 1,
#                 "top_p": 0.95,
#                 "top_k": 40,
#                 "max_output_tokens": 8192,
#             },
#         )
#         print(response.text)
#         return jsonify(json.loads(response.text))
        
#     except Exception as e:
#         print(e)
#         return jsonify({"error": str(e)})

@app.route("/generate-content", methods=["POST"])
def generate_content():
    data = request.get_json()
    web_content = data.get("data")

    urllib.request.urlretrieve(web_content, "image.jpeg") 
  
    img = Image.open("image.jpeg") 

    try:
        response = client.models.generate_content(
            model= "gemini-2.0-flash-exp",
            contents=[SP, img],
            config={
                "response_mime_type": "application/json",
                "response_schema": WebsiteAnalysis,
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            },
        )
        print(response.text)
        return jsonify(json.loads(response.text))
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})