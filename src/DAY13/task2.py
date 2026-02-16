import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "SquareFootage": [
        600, 750, 900, 1100, 1300, 1500,
        1700, 1900, 2100, 2300, 2500, 2800
    ],
    "Price": [
        150000, 180000, 210000, 250000, 280000, 320000,
        360000, 400000, 440000, 470000, 520000, 600000
    ],
    "City": [
        "Bangalore", "Mumbai", "Delhi", "Chennai",
        "Hyderabad", "Bangalore", "Mumbai", "Delhi",
        "Chennai", "Hyderabad", "Bangalore", "Mumbai"
    ]
}

df = pd.DataFrame(data)


plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Scatter Plot: SquareFootage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()



plt.figure(figsize=(8,5))
sns.boxplot(x="City", y="Price", data=df)
plt.title("Boxplot: City vs Price")
plt.xlabel("City")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.show()

print("Observation:")
print("As SquareFootage increases, Price seems to increase.")
