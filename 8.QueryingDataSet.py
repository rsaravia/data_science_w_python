import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

# Querying DataSet
# print(nba["year_id"] > 2010)
current_decade = nba[nba["year_id"]>2010]
print ("current_decade shape: ", current_decade.shape)

print("---")

# Fields Not Null
games_with_notes = nba[nba["notes"].notnull()]
print ("games with notes shape: ", games_with_notes.shape)
games_with_notes = nba[nba["notes"].notna()]
print ("games with notes shape: ", games_with_notes.shape)


print("---")


# String Filtering (endswith)
ers = nba[nba["fran_id"].str.endswith("ers")]
print ("Ended with ERS: ", ers.shape)