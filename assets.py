import pandas as pd

def get_player_data():
    return pd.read_csv(r"csv_vault\Characters_Players.csv")