import os
from dotenv import load_dotenv
from google import genai

from tools.calculator import calculator
from tools.weather import get_weather
from tools.text_utility import text_utility
from tools.wikipedia_tool import wikipedia_summary

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Define the tools Gemini can use
tools = [
    calculator,
    get_weather,
    text_utility,
    wikipedia_summary
]


# Create a chat with the tools
chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "tools": tools
    }
)


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)

    print("Agent:", response.text)