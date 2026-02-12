import pandas as pd

# 1. Load dataset
df = pd.read_csv("customer_information.csv")

# 2. Shape before cleaning
print("Shape before cleaning:", df.shape)

# 3. Missing values report
print("\nMissing Values Report:")
print(df.isna().sum())

# 4. Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['number']).columns

for col in numeric_cols:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

# 5. Remove duplicate rows (all columns match)
df_cleaned = df.drop_duplicates()

# 6. Shape after cleaning
print("\nShape after cleaning:", df_cleaned.shape)
