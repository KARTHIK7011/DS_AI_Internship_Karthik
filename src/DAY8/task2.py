import numpy as np

# Step 1: Create 1D array from 0 to 23
data = np.arange(24)

# Step 2: Reshape into (4, 3, 2)
reshaped = data.reshape(4, 3, 2)

# Step 3: Transpose to (4, 2, 3)
transposed = reshaped.transpose(0, 2, 1)

# Step 4: Print results
print("Final Shape:", transposed.shape)
print("Final Array:\n", transposed)
