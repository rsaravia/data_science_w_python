
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

df = nba.copy()
print("Shape: ", df.shape)

# Define new columns based on the existing ones
df["difference"] = df.pts - df.opp_pts
print("Shape: ", df.shape)

print("---")

# Renamed
renamed_df = df.rename(columns={"game_result":"result","game_location":"location"})
print(df.info())
print(renamed_df.info())


print("---")

#Drop columns
elo_columns = ["elo_i","elo_n","opp_elo_i","opp_elo_n"]
df.drop(elo_columns, inplace=True, axis=1)
print("new df shape: ", df.shape)