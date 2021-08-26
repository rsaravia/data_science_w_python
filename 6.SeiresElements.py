import pandas as pd

city_revenues = pd.Series([4200, 8000, 6500], index=["Amsterdam","Toronto","Tokyo"])

#Accesando por indice
print(city_revenues[1])
#Accesando por label
print(city_revenues["Toronto"])

# Using .loc and .iloc
color = pd.Series(
    ["red","purple","blue","green","yellow"],
    index=[1,2,3,5,8]
)

print("---")

# .loc means "label index"
print(color.loc[1])
# .iloc means "positional index"
print(color.iloc[1])

