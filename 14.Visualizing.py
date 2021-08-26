import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

import matplotlib.pyplot as plt

series = nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum
print(series)


fig = plt.figure()
ax = plt.axes()
ax.plot(series)