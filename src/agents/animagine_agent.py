from uagents import Agent,Context
import requests
from PIL import Image
import io
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path("../.env"))
animagine_agent = Agent(
    name="Animagine Agent",
    port=8001,
    seed="Gemini Agent secret phrase",
    endpoint=["http://localhost:8001/submit"],
)
ANIMAGINE_KEY = os.getenv("ANIMAGINE_KEY")
API_URL = "https://api-inference.huggingface.co/models/ogkalu/Comic-Diffusion"
headers = {"Authorization": f"Bearer {ANIMAGINE_KEY}"}
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
# Prompt user for input query
user_query = input("Enter your query: ")

# Make a query using user input
image_bytes = query({"inputs": user_query})
# You can access the image with PIL.Image for example
image = Image.open(io.BytesIO(image_bytes))
# Create a directory if it doesn't exist
folder_path = "images"
os.makedirs(folder_path, exist_ok=True)

# Save the image to a file in the specified folder
file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
image_path = os.path.join(folder_path, f"{file_count}.jpg")
image.save(image_path)

print(f"Image saved at: {image_path}")