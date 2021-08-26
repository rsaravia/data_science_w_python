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

print(city_data)
# Means: Series is like Columns (fields), and index on each series is register
# DataFrame create each register with the union of index of two columns (fields)


print("Index: ", city_data.index)
print("Values: ", city_data.values)

# Ejes
print("Axes: ", city_data.axes)
#First cols and them columns


# DataFrame is like a Dictionary
# You can access to data naming by Column Name
print("Keys: ", city_data.keys())
print("Amsterdam Data:", city_data["revenue"].values)
