
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]


unique_users = set(raw_logs)

print("Is ID05 present?", "ID05" in unique_users)

# Count comparison
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))

# Show unique users
print("Unique User IDs:", unique_users)
