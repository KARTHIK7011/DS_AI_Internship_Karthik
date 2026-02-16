import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# Dataset (Dictionary Format)
# -----------------------------------
data = {
    "SquareFootage": [600, 750, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2800],
    "Bedrooms":      [1,   2,   2,   3,    3,    3,    4,    4,    4,    5,    5,    5],
    "Price":         [150000, 180000, 210000, 250000, 280000, 320000, 360000, 400000, 440000, 470000, 520000, 800000]
}

df = pd.DataFrame(data)

# -----------------------------------
# 1. Correlation Matrix + Heatmap
# -----------------------------------
corr_matrix = df.corr()

plt.figure(figsize=(6,5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

# -----------------------------------
# 2. Find highly correlated variables (> 0.8)
# -----------------------------------
print("Highly Correlated Pairs (Correlation > 0.8):")
for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2 and corr_matrix.loc[col1, col2] > 0.8:
            print(f"{col1} and {col2} -> {corr_matrix.loc[col1, col2]:.2f}")

# -----------------------------------
# 3. Boxplot to detect Outliers (Price)
# -----------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price (Outlier Detection)")
plt.ylabel("Price")
plt.show()
