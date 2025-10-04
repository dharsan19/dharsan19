import requests
import json
import os

monkey_type_url = "https://api.monkeytype.com/users/personalBests?mode=time&mode2=30"
# monkeytype_api_key = os.environ.get("MONKEYTYPE_API_KEY")  # safer via GitHub Secrets
monkeytype_api_key = "NjhlMGMwOTNjMmM1MDA0Y2Q0YjY0ZDI3Lkd1eVJYRl9IaTJXSEV5SW9WR01qeDJNbUtrWGhTcThp"


headers = {
    "Authorization": "ApeKey " + monkeytype_api_key,
}

response = requests.get(monkey_type_url, headers=headers)
data = response.json()

# Pick the top entry (highest WPM personal best for 30s test)
best_entry = max(data["data"], key=lambda x: x["wpm"])
wpm = round(best_entry["wpm"])

# Convert to Shields.io badge format
badge_json = {
    "schemaVersion": 1,
    "label": "monkeytype WPM",
    "message": str(wpm),
    "color": "yellow",
    "style": "for-the-badge",
    "namedLogo": "monkeytype",

}

with open("assets/stats.json", "w") as f:
    json.dump(badge_json, f)

print(f"Updated stats.json with WPM: {wpm}")