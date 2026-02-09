
name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name} | Daily Goal: {goal}\n")

print("Saved to journal.txt")
file=open("journal.txt","r")
content=file.read()
print(content)
file.close()
