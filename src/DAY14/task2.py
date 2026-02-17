# Feature Scaling Demo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [22, 25, 28, 30, 35, 40, 45, 50, 29, 31, 38, 42],
    "Salary": [25000, 30000, 32000, 40000, 50000, 65000, 70000, 90000, 45000, 52000, 58000, 62000]
}

df = pd.DataFrame(data)
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)


minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)


plt.figure(figsize=(12,5))


#plt.subplot(1, 3, 1)
plt.hist(df["Salary"], bins=8)
plt.title("Original Salary")
plt.show()

#plt.subplot(1, 3, 2)
plt.hist(df_standardized["Salary"], bins=8)
plt.title("Standardized Salary")
plt.show()

#plt.subplot(1, 3, 3)
plt.hist(df_normalized["Salary"], bins=8)
plt.title("Normalized Salary")

plt.tight_layout()
plt.show()



