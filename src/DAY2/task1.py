# Ask user details
name = input("Enter your name: ")
age = input("Enter your current age: ")

# Convert age to integer
age = int(age)

# Calculate age in 2030 (2026 → 2030 = +4 years)
new_age = age + 4

# Print result
print(f"Hey {name}, you will be {new_age} years old in 2030!")
