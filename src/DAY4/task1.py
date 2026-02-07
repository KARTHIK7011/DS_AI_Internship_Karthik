contacts = {
    "Karthik": "9876543210",
    "Ravi": "9123456780",
    "Anu": "9012345678"
}


contacts["Neha"] = "9988776655"


contacts["Ravi"] = "9000000000"


print("Lookup Existing:", contacts.get("Karthik", "Contact not found"))
print("Lookup Missing:", contacts.get("Arjun", "Contact not found"))

print("\nContact List:")

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
