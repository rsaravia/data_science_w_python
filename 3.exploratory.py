import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

# Verificar por que los laker jugaron  6024 partidos
# pero solo 5078 por Los Angeles Lakers

value_counts = nba["team_id"].value_counts()
value2_counts = nba["fran_id"].value_counts()

print("Value Counts of Team Id: ", value_counts)
print("Value Counts of Fran Id: ", value2_counts)

# Encontrar cuales son los otros lakers

value3 = nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts()
print(value3)

# Encontrar

nba["date_played"] = pd.to_datetime(nba["date_game"])
minimo = nba.loc[nba["team_id"] == "BOS", "date_played"].min()
maximo = nba.loc[nba["team_id"] == "BOS", "date_played"].max()
print("Minimo: ", minimo)
print("Maximo: ", maximo)
# differencia = nba.loc[nba["team_id"] == "MNL", "date_played"].agg(("min","max"))
# print("Diferencia: ", differencia)
