#Grouping and aggregation functions
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")


points = nba["pts"]
print("Type: ", type(points))
print("Sum: ", points.sum())
print("Max: ", points.max())
print("Min: ", points.min())
print("Ave: ", points.mean())

print("---")

# Agrupamientos: es decir, agrupa por una categoria y luego suma
# Es como lo que hace una tabla dinamica
print("Agrupamiento: ")
print(nba.groupby("fran_id", sort=False)["pts"].sum())


print("---")

# Agrupamiento de multiples columnas
print("Agrupamiento multiples columnas")
print(nba[(nba["fran_id"] == "Spurs") &
          (nba["year_id"] > 2010)
          ].groupby(["year_id","game_result"])["game_id"].count())