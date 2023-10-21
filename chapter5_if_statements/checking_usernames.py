current_users = ["Mathis", "Alice", "Sam", "Claire", "Marc"]

current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

new_users = ["Mario", "Luigi", "MATHIS", "alice", "Sam"]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} is unavailable. Please pick another.")
    else:
        print(f"The username {new_user} is available.")