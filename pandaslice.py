import pandas as pd

data = {
    "Name": ["Ravi", "Raju", "Sita", "Arun", "Meena"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 78, 92, 88, 90]
}

df = pd.DataFrame(data)

print("Sorted by Marks:\n", df.sort_values(by="Marks"))

print("\nSlicing Rows:\n", df[1:4])

print("\nSelecting Columns:\n", df[["Name", "Marks"]])
