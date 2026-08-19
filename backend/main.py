from tools.calculator import calculator
from tools.weather import get_weather
from tools.text_utility import text_utility


# Calculator
print("Calculator:")
print(calculator(10, 5, "add"))


# Text Utility
print("\nText Utility:")
print(text_utility("Hello world", "word_count"))


# Weather
print("\nWeather:")
print(get_weather(19.99, 73.79))