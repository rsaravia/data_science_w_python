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

# Se pueden llamar de igual forma
print("revenue: ", city_data["revenue"])
print("revenue: ", city_data.revenue)