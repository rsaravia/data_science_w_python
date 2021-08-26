import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")
print("Type: ", type(nba))
print("Len: ", len(nba))
print("Shape: ", nba.shape)
nba.info()
print(nba.head())