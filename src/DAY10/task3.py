import pandas as pd

data = {
    "Customer": ["John", "Alice", "Bob", "Emma", "David"],
    "Location": [" New York", "new york", "NEW YORK ", " New York ", "new york"]
}

df = pd.DataFrame(data)

print("Unique Locations BEFORE cleaning:")
print(df["Location"].unique())


df["Location"] = df["Location"].str.strip().str.title()

# (Alternative: use .str.lower() if you prefer lowercase)
# df["Location"] = df["Location"].str.strip().str.lower()

# 3. Check unique values AFTER cleaning
print("\nUnique Locations AFTER cleaning:")
print(df["Location"].unique())
