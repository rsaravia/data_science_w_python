
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

print(nba.info())
nba["date_game"] = pd.to_datetime(nba["date_game"])
print(nba.info())

print("---")

print("Unique Num: ", nba["game_location"].nunique())
print("Unique values: ", nba["game_location"].value_counts())