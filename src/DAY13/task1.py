import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Price": [
        213159.6887, 169942.2730, 226616.4536, 287397.7070,
        163032.4432, 163034.5596, 292610.9877, 234996.9233,
        150799.1301, 217944.5810, 151292.2114, 151108.5945
    ],
    "City": [
        "Bangalore", "Mumbai", "Hyderabad", "Bangalore",
        "Chennai", "Chennai", "Bangalore", "Hyderabad",
        "Bangalore", "Bangalore", "Chennai", "Delhi"
    ]
}

df = pd.DataFrame(data)

print(df.head())


plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)


if skewness > 0:
    print("Price distribution is Right-Skewed (positive skew).")
elif skewness < 0:
    print("Price distribution is Left-Skewed (negative skew).")
else:
    print("Price distribution is Symmetrical (normal-like).")


plt.figure(figsize=(8,5))
sns.countplot(x="City", data=df, order=df["City"].value_counts().index)
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


most_common_city = df["City"].value_counts().idxmax()
print("Most frequent City:", most_common_city)
