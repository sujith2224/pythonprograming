import pandas as pd
data = {
    "Name": ["Ravi", "Raju", "Sita", "Arun", None],
    "Age": [20, 21, None, 22, 20],
    "Marks": [85, 78, 92, None, 90]
}
df = pd.DataFrame(data)
df["Marks"] = df["Marks"].fillna(0)
df = df.dropna()
df["Total"] = df["Marks"] + 10
print(df)
