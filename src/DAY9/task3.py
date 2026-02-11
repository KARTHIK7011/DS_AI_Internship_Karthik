import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove leading and trailing spaces
cleaned = usernames.str.strip()

lowercase = cleaned.str.lower()


contains_a = lowercase.str.contains('a')

# Output
print("Original Usernames:")
print(usernames)

print("\nAfter Removing Spaces:")
print(cleaned)

print("\nLowercase Usernames:")
print(lowercase)

print("\nNames containing letter 'a':")
print(contains_a)
