import pandas as pd

df = pd.read_csv("customer_orders.csv")

# 2. Check initial data types
print("Initial Data Types:\n")
print(df.dtypes)

# 3. Clean Price column (remove '$' and convert to float)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# 4. Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# 5. Check updated data types
print("\nUpdated Data Types:\n")
print(df.dtypes)

# 6. Example operations (to prove data is usable)
print("\nAverage Price:", df["Price"].mean())
print("Latest Date:", df["Date"].max())
