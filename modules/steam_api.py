import requests

STEAM_API_KEY = "1D53AE707CE550BDA33CAD2F44C2058C"

# Search game by name
def search_game(query):
    url = f"https://steamcommunity.com/actions/SearchApps/{query}"
    response = requests.get(url)
    return response.json()

# Get game details by Steam AppID
def get_game_details(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.get(url)
    data = response.json()

    if data[str(appid)]["success"]:
        return data[str(appid)]["data"]
    
    return None

# Get current player count
def get_player_count(appid):
    url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={appid}&key={STEAM_API_KEY}"
    response = requests.get(url)
    return response.json()
