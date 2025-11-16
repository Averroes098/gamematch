import json
import os

# --- Loader utama: dipanggil app.py ---
def load_games(base_dir=None):
    if base_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    games_path = os.path.join(base_dir, "data", "games.json")
    with open(games_path, "r", encoding="utf-8") as f:
        return json.load(f)


# --- Filter game berdasarkan RAM ---
def match_games(laptop, games):
    playable = []

    for g in games:
        if laptop["ram"] >= g["ram"]:
            playable.append(g)

    return playable


# --- Ambil laptop berdasarkan nama ---
def get_laptop_by_name(name, laptops):
    return next((l for l in laptops if l["name"] == name), None)


# --- Ambil semua laptop dari JSON ---
def get_all_laptops():
    with open("data/laptops.json", "r", encoding="utf-8") as f:
        return json.load(f)


# --- Ambil semua game dari JSON ---
def get_all_games():
    with open("data/games.json", "r", encoding="utf-8") as f:
        return json.load(f)


# --- Analisis laptop manual ---
def analyze_manual_laptop(cpu, gpu, ram, games):
    manual_laptop = {
        "name": "Manual Input",
        "cpu": cpu,
        "gpu": gpu,
        "ram": ram
    }
    return match_games(manual_laptop, games)


# --- Analisis laptop predefined ---
def analyze_predefined_laptop(laptop_name, laptops, games):
    selected = get_laptop_by_name(laptop_name, laptops)
    if selected:
        return match_games(selected, games)
    return []
