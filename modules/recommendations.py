"""
Module untuk memberikan rekomendasi game berdasarkan spesifikasi laptop
"""

RECOMMENDED_GAMES = [
    {"name": "Minecraft", "ram": 4, "category": "Casual", "description": "Game sandbox yang bisa dimainkan di berbagai hardware"},
    {"name": "Valorant", "ram": 4, "category": "Esports", "description": "FPS ringan yang bisa berjalan smooth di laptop entry-level"},
    {"name": "Fortnite", "ram": 8, "category": "Battle Royale", "description": "Battle royale populer, membutuhkan GPU yang decent"},
    {"name": "Dota 2", "ram": 4, "category": "MOBA", "description": "MOBA classic yang ringan dan esports-focused"},
    {"name": "Counter-Strike 2", "ram": 8, "category": "Esports", "description": "Shooter klasik, bisa berjalan di hardware lama"},
    {"name": "League of Legends", "ram": 4, "category": "MOBA", "description": "MOBA paling populer, requirements rendah"},
    {"name": "GTA V", "ram": 8, "category": "Action", "description": "Open-world action game yang iconic"},
    {"name": "Cyberpunk 2077", "ram": 12, "category": "RPG", "description": "RPG futuristik dengan grafis stunning"},
    {"name": "The Witcher 3", "ram": 8, "category": "RPG", "description": "RPG fantasy terbaik dengan cerita menarik"},
    {"name": "Hogwarts Legacy", "ram": 16, "category": "RPG", "description": "RPG Harry Potter dengan grafis impressive"},
    {"name": "Elden Ring", "ram": 12, "category": "Action RPG", "description": "Action RPG challenging dari FromSoftware"},
    {"name": "Baldur's Gate 3", "ram": 16, "category": "RPG", "description": "RPG masterpiece dengan gameplay mendalam"},
]

def get_game_recommendations(laptop_ram):
    """
    Get game recommendations based on laptop RAM
    Returns list of games suitable for the laptop
    """
    recommendations = []
    
    for game in RECOMMENDED_GAMES:
        if laptop_ram >= game["ram"]:
            recommendations.append(game)
    
    # Sort by RAM requirement ascending (playable games first)
    recommendations.sort(key=lambda x: x["ram"])
    
    return recommendations[:6]  # Return top 6 recommendations


def get_difficulty_level(laptop_ram):
    """
    Determine what difficulty level of games the laptop can handle
    """
    if laptop_ram >= 16:
        return "High-End", "AAA games dengan grafis ultra"
    elif laptop_ram >= 12:
        return "Mid-High", "AAA games dengan grafis high"
    elif laptop_ram >= 8:
        return "Mid-Range", "Game populer dengan grafis medium"
    elif laptop_ram >= 4:
        return "Entry-Level", "Casual & esports games"
    else:
        return "Very Low", "Game ringan saja"
