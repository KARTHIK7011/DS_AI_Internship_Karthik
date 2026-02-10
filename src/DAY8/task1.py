import numpy as np

# Step 1: Create 5x3 array (5 students, 3 subjects) with scores 50–100
scores = np.random.randint(50, 101, size=(5, 3))

# Step 2: Column-wise mean (mean of each subject)
mean_per_subject = np.mean(scores, axis=0)

# Step 3: Subtract mean using broadcasting (center the data)
centered_scores = scores - mean_per_subject

# Step 4: Print results
print("Original Scores:\n", scores)
print("\nMean per Subject:\n", mean_per_subject)
print("\nCentered Scores (After Broadcasting):\n", centered_scores)
