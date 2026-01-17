import requests
import datetime
import json

DEST_FILE = "_data/mlb_standings.json"

def fetch_mlb_standings():
    # MLB Records and Stats API URL
    url = "http://statsapi.mlb.com/api/v1/standings"
    params = {
        "leagueId": "103,104",  # AL (103), NL (104)
        "season": datetime.datetime.now().year,  # Current year
        "standingsTypes": "regularSeason"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        standings = response.json()
        save_standings_to_file(standings)
        print("Standings fetched successfully.")
    else:
        print(f"Failed to fetch standings. HTTP {response.status_code}")

def save_standings_to_file(standings):
    with open(DEST_FILE, "w") as json_file:
        json.dump(standings, json_file, indent=4)
    print(f"Standings saved to {DEST_FILE}")

if __name__ == "__main__":
    fetch_mlb_standings()