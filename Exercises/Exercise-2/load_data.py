import pandas as pd

df = pd.read_csv("climatological-data-14:03.csv")

df_sorted = df.sort_values("HourlyDryBulbTemperature", axis=0, ascending=True )

print(df_sorted.head(10))

