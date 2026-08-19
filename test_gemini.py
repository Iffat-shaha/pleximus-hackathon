import os
from dotenv import load_dotenv
from google import genai

load_dotenv("backend/.env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Reply only with: Gemini is working"
)

print(response.text)