

# Step 1 — Import Libraries
import numpy as np
import pandas as pd



np.random.seed(42)

data = pd.DataFrame({
    "Values": np.random.normal(loc=50, scale=10, size=1000)
})

# Add a few extreme values manually (to see outliers clearly)
data.loc[1001] = 120
data.loc[1002] = 130
data.loc[1003] = -20


mu = data["Values"].mean()
sigma = data["Values"].std()

print("Mean (μ):", round(mu, 2))
print("Std Dev (σ):", round(sigma, 2))



data["z_score"] = (data["Values"] - mu) / sigma



outliers = data[np.abs(data["z_score"]) > 3]

print("\nNumber of Outliers Detected:", len(outliers))
print("\nOutlier Rows:")
print(outliers)



print("\nTop Extreme Values:")
print(data.sort_values("z_score", ascending=False).head())

print("\nLowest Extreme Values:")
print(data.sort_values("z_score").head())


print("\n===== INSIGHT =====")
print("Z-score measures how many standard deviations a value is from the mean.")
print("|Z| > 3 usually indicates a statistical outlier.")
print("Z-score allows comparison across different units (e.g., exam score vs height).")
