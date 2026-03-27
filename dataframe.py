import pandas as pd
df = pd.read_csv("data.csv")
print("HEAD:\n", df.head())
print("\nTAIL:\n", df.tail())
print("\nINFO:\n")
print(df.info())
print("\nDESCRIBE:\n", df.describe())

