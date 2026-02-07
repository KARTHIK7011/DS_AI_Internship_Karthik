# Ask for total bill (float allows decimals)
total_bill = float(input("Enter total bill amount: "))

# Ask for number of people
people = int(input("Enter number of people: "))

# Calculate share per person
share = total_bill / people

# Output result
print(f"Total Bill: {total_bill}. Each person pays: {share}")

# Bonus: Check data types
print("Type of total_bill:", type(total_bill))
print("Type of people:", type(people))
print("Type of share:", type(share))
