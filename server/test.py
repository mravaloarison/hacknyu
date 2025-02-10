import os
import requests
import pathlib
from PIL import Image
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

IMG = """
""" 

img_bytes = requests.get(IMG).content

img_path = pathlib.Path('jetpack.png')
img_path.write_bytes(img_bytes)


image = Image.open(img_path)
image.thumbnail([512,512])

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        image,
        "Write a short and engaging blog post based on this picture."
    ]
)

print(response.text)