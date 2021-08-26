import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

# Create a new series
revenues = pd.Series([5555, 7000, 1980])

print("Values: ", revenues.values)
print("Inex: ", revenues.index)

print("---")

# Series with String Index
city_revenues = pd.Series([4200, 8000, 6500], index=["Amsterdam","Toronto","Tokyo"])
print("City Revenues: ", city_revenues)

print("---")


# Series from Dictionary
city_employee_count = pd.Series({"Amsterdam":5,"Tokyo":8})
print("City Employees: ", city_employee_count)

# Accesing by Keys
print("City Employee Keys: ", city_employee_count.keys())
for i in city_employee_count.keys():
    print(i)
print("is 'Tokyo' in city_employee_count: ", "Tokyo" in city_employee_count)
print("Un valor: ", city_employee_count[0])
print("Un valor: ", city_employee_count[1])