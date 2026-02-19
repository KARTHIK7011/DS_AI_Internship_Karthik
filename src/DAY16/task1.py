

# Step 1 — Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
np.random.seed(42)



# Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Income)
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Create DataFrame
df = pd.DataFrame({
    "Heights_Normal": heights,
    "Incomes_RightSkewed": incomes,
    "Scores_LeftSkewed": scores
})



plt.figure(figsize=(15, 4))

# Normal Distribution
plt.subplot(1, 3, 1)
sns.histplot(df["Heights_Normal"], kde=True)
plt.title("Normal Distribution (Heights)")

# Right-Skewed Distribution
plt.subplot(1, 3, 2)
sns.histplot(df["Incomes_RightSkewed"], kde=True)
plt.title("Right-Skewed Distribution (Income)")

# Left-Skewed Distribution
plt.subplot(1, 3, 3)
sns.histplot(df["Scores_LeftSkewed"], kde=True)
plt.title("Left-Skewed Distribution (Exam Scores)")

plt.tight_layout()
plt.show()



print("\n===== MEAN vs MEDIAN COMPARISON =====")

for col in df.columns:
    mean_val = df[col].mean()
    median_val = df[col].median()

    print(f"\nDataset: {col}")
    print("Mean   :", round(mean_val, 2))
    print("Median :", round(median_val, 2))

    if mean_val > median_val:
        print("→ Right-Skewed (Positive Skew)")
    elif mean_val < median_val:
        print("→ Left-Skewed (Negative Skew)")
    else:
        print("→ Normal / Symmetric")



print("\n===== INSIGHT =====")
print("If Mean > Median → Right-Skewed")
print("If Mean < Median → Left-Skewed")
print("If Mean ≈ Median → Normal Distribution")
print("\nSkewed data can bias ML models. Consider transformations like log or sqrt if needed.")
