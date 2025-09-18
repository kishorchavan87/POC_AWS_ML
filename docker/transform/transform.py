import pandas as pd

df = pd.read_csv("/app/data/raw_data.csv")
df = df.dropna()
df.to_csv("/app/data/clean_data.csv", index=False)
print("Transformed and saved clean CSV")
