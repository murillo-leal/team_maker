import decimal




def generate_team(players:list):
    for player in players:
        player['media'] = Decimal(player['Tier'])