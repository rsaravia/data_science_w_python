

import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

# Borrar todos los registros que tengan algun campo nulo
print("original shape: ", nba.shape)
rows_without_missing_data = nba.dropna()
print("shape dropped: ",rows_without_missing_data.shape)

print("---")

# Borrar la columan con campos nulos
print("original shape:", nba.shape)
rows_without_missing_columns = nba.dropna(axis=1)
print("shape dropped: ",rows_without_missing_columns.shape)

print("---")

# Reemplazar contenido
print("original shape:", nba.shape)
data_with_default_notes = nba.copy()
data_with_default_notes["notes"].fillna(value="nada", inplace=True)
print("shape dropped: ",data_with_default_notes.shape)


print("---")

# El total de registros con pts = 0
print(nba[nba["pts"] == 0])
