import pandas as pd

with open("shopping_trends.csv", "r") as file:
    data = file.read()
    pd_data = pd.DataFrame(data)