from src.infrastructure.load_players import load_players


def team_maker():
    players = load_players()
    teams = generate_teams(players)
