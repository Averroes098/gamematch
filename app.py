import os
import json
import re
from flask import Flask, render_template, request, session
from modules.laptop_reader import load_laptops
from modules.matcher import match_games_to_laptop
from modules.steam_api import search_game, get_game_details
from modules.compatibility import analyze_compatibility
from modules.recommendations import get_game_recommendations, get_difficulty_level

app = Flask(__name__)
app.secret_key = "gamematch_secret_key_2025"
app.jinja_env.cache = {}  # Disable template caching
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load dataset
LAPTOPS = load_laptops(BASE_DIR)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/input-laptop", methods=["GET", "POST"])
def input_laptop():
    if request.method == "POST":
        laptop_name = request.form.get("laptop_name")
        
        # If laptop selected from database
        if laptop_name:
            user_laptop = None
            for laptop in LAPTOPS:
                if laptop["name"] == laptop_name:
                    user_laptop = laptop
                    break
            if not user_laptop:
                return render_template("input_laptop.html", laptops=LAPTOPS, error="Laptop tidak ditemukan")
        else:
            # Manual input
            cpu = request.form.get("cpu", "").strip()
            gpu = request.form.get("gpu", "").strip()
            ram_str = request.form.get("ram", "").strip()
            
            if not cpu or not gpu or not ram_str:
                return render_template("input_laptop.html", laptops=LAPTOPS, error="Harap isi semua field manual atau pilih laptop dari database")
            
            try:
                ram = int(ram_str)
            except ValueError:
                return render_template("input_laptop.html", laptops=LAPTOPS, error="RAM harus berupa angka")
            
            user_laptop = {
                "name": f"Custom ({cpu})",
                "cpu": cpu,
                "gpu": gpu,
                "ram": ram
            }

        session["current_laptop"] = user_laptop
        return render_template(
            "result.html",
            laptop=user_laptop
        )

    return render_template("input_laptop.html", laptops=LAPTOPS)


@app.route("/compare/<appid>")
def compare_laptop_game(appid):
    try:
        laptop = session.get("current_laptop")
        if not laptop:
            return render_template("error.html", message="Silakan pilih laptop terlebih dahulu"), 400
        
        game = get_game_details(appid)
        if not game:
            return render_template("error.html", message="Game tidak ditemukan"), 404
        
        # Analisis kompatibilitas
        # Extract RAM requirements dari game requirements (jika ada)
        game_min_ram = None
        game_rec_ram = None
        
        if game and isinstance(game, dict) and game.get("pc_requirements"):
            try:
                min_text = game["pc_requirements"].get("minimum", "")
                rec_text = game["pc_requirements"].get("recommended", "")
                
                # Cari angka RAM di teks (simple parsing)
                if min_text:
                    min_match = re.search(r'(\d+)\s*(?:GB)?.*?(?:RAM|Memory)', str(min_text), re.IGNORECASE)
                    if min_match:
                        game_min_ram = int(min_match.group(1))
                
                if rec_text:
                    rec_match = re.search(r'(\d+)\s*(?:GB)?.*?(?:RAM|Memory)', str(rec_text), re.IGNORECASE)
                    if rec_match:
                        game_rec_ram = int(rec_match.group(1))
            except Exception as e:
                print(f"Error parsing RAM requirements: {e}")
        
        compatibility = analyze_compatibility(
            laptop.get("ram", 0),
            game_min_ram,
            game_rec_ram
        )
        
        return render_template(
            "compare.html",
            laptop=laptop,
            game=game,
            compatibility=compatibility
        )
    except Exception as e:
        print(f"Error in compare_laptop_game: {e}")
        return render_template("error.html", message=f"Terjadi error: {str(e)}"), 500


@app.route("/steam-search", methods=["GET", "POST"])
def steam_search():
    laptop = session.get("current_laptop")
    recommendations = []
    difficulty = None
    
    if laptop:
        recommendations = get_game_recommendations(laptop.get("ram", 0))
        difficulty = get_difficulty_level(laptop.get("ram", 0))
    
    if request.method == "POST":
        query = request.form.get("query")
        results = search_game(query)
        return render_template("steam_result.html", results=results, current_laptop=laptop)
    
    return render_template("steam_search.html", current_laptop=laptop, recommendations=recommendations, difficulty=difficulty)


@app.route("/steam-details/<appid>")
def steam_details(appid):
    laptop = session.get("current_laptop")
    details = get_game_details(appid)
    return render_template("steam_details.html", game=details, laptop=laptop)


#if __name__ == "__main__":
#    app.run(debug=True)
