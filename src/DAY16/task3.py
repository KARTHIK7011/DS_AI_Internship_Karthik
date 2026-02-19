# Step 1 — Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
np.random.seed(42)


# Exponential distribution → strong right skew
population = np.random.exponential(scale=50, size=10000)

# Visualize original skewed data
plt.figure()
sns.histplot(population, kde=True)
plt.title("Original Population Distribution (Skewed)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()



sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)  # sample size = 30
    sample_means.append(sample.mean())


plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()



print("Population Mean:", round(population.mean(), 2))
print("Mean of Sample Means:", round(np.mean(sample_means), 2))


print("\n===== OBSERVATION =====")
print("1. Original data is skewed (not normal).")
print("2. Distribution of sample means becomes bell-shaped (normal).")
print("3. Mean of sample means ≈ Population mean.")
print("\nThis is the Central Limit Theorem in action.")
