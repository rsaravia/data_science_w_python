import pandas as pd

# Dictionary keys is Column Names
import pandas as pd

# A serie
city_revenues = pd.Series(
        [4200, 8000, 6500],
        index=["Amsterdam", "Toronto", "Tokyo"]
        )

# A serie
city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})

city_data = pd.DataFrame(
    {"revenue": city_revenues,
     "employee_count": city_employee_count}
)



further_city_data = pd.DataFrame(
    {"revenue": [7000, 3400], "employee_count": [2,2]},
    index=["New York", "Barcelona"]
)

all_city_data = pd.concat([city_data, further_city_data], sort=False)
print(all_city_data)


print("---")


city_countries = pd.DataFrame(
    {"country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
     "capital": [1, 1, 0, 0, 0]},
     index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"]
    )
cities = pd.concat([all_city_data, city_countries], axis=1, sort=False)
print(cities)

city_countries = pd.DataFrame(
    {"country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
     "capital": [1, 1, 0, 0, 0]},
     index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"]
    )
cities2 = pd.concat([all_city_data, city_countries], axis=1, join="inner")
print(cities2)

print("---")

countries = pd.DataFrame({
    "population_millions": [17, 127, 37],
    "continent": ["Europe", "Asia", "North America"]
    }, index= ["Holland", "Japan", "Canada"])
otra = pd.merge(cities2, countries, left_on="country", right_index=True)
print(otra)
