import decimal




def generate_teams(players:list):
    for player in players:
        player['media'] = decimal(player['Tier']) + decimal(player['Nota']) / 2

    finished = Fale
    while not finished:
        