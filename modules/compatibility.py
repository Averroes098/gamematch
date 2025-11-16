"""
Module untuk menganalisis kompatibilitas laptop dengan game
"""

def analyze_compatibility(laptop_ram, game_min_ram=None, game_rec_ram=None):
    """
    Analisis kompatibilitas berdasarkan RAM
    Returns: dict dengan status dan pesan
    """
    status = {
        "minimum": None,
        "recommended": None,
        "overall": None,
        "message": ""
    }
    
    if game_min_ram and laptop_ram >= game_min_ram:
        status["minimum"] = "✅ LANCAR"
    elif game_min_ram:
        status["minimum"] = f"❌ TIDAK LANCAR (kurang {game_min_ram - laptop_ram}GB)"
    
    if game_rec_ram and laptop_ram >= game_rec_ram:
        status["recommended"] = "✅ LANCAR - OPTIMAL"
    elif game_rec_ram:
        status["recommended"] = f"⚠️ TERBATAS (kurang {game_rec_ram - laptop_ram}GB)"
    
    # Tentukan overall status
    if status["recommended"] and "✅" in status["recommended"]:
        status["overall"] = "excellent"
        status["message"] = "Game akan berjalan dengan sempurna di laptop Anda dengan setting high/ultra!"
    elif status["minimum"] and "✅" in status["minimum"]:
        status["overall"] = "playable"
        status["message"] = "Game dapat berjalan di laptop Anda, tapi mungkin perlu setting medium untuk smooth."
    else:
        status["overall"] = "poor"
        status["message"] = "Game mungkin tidak lancar atau tidak bisa berjalan di laptop Anda."
    
    return status
