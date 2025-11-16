def match_games_to_laptop(laptop, games):
    playable = []

    for game in games:
        if laptop["ram"] >= game["ram"]:
            playable.append(game)

    return playable
