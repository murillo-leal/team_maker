import pandas as pd
import os
import csv


def load_players():
        with open('players.csv') as f:
            file_data=csv.reader(f)
            headers=next(file_data)
            return [dict(zip(headers,i)) for i in file_data]



