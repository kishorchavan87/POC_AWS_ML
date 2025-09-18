import requests
import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df = pd.read_csv(url)

df.to_csv("/app/data/raw_data.csv", index=False)
print("Data extracted and saved locally")
