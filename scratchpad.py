import assets
import pandas as pd

players = assets.get_player_data()

print(players.iloc[:1])