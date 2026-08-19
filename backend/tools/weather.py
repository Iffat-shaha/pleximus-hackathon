import requests


def get_weather(latitude: float, longitude: float) -> dict | str:
    """Get current weather using latitude and longitude."""

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true"
    )

    response = requests.get(url)

    print("Raw API response:")
    print(response.text)

    if response.status_code != 200:
        return "Error: Unable to fetch weather data"

    data = response.json()

    if "current_weather" not in data:
        return "Error: Weather data unavailable"

    weather = data["current_weather"]

    return {
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "weathercode": weather["weathercode"]
    }