import requests


def wikipedia_summary(topic: str) -> str:
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + topic.replace(" ", "_")

    response = requests.get(
        url,
        headers={"User-Agent": "PleximusAIHackathon/1.0"}
    )

    if response.status_code != 200:
        return f"Could not find a Wikipedia page for '{topic}'."

    data = response.json()

    return data.get("extract", f"No summary found for '{topic}'.")


if __name__ == "__main__":
    print(wikipedia_summary("Artificial Intelligence"))