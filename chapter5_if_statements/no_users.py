users = ["Mathis", "Alice", "Sam", "admin", "Claire", "Marc"]
print(f"users = {users}")

if users:
    for user in users:
        if user == "admin":
            print(f"Hello, {user}. Would you like to see a status report?")
        else:
            print(f"Hello {user}, thanks for logging in.")
else:
    print("We need to find more users!")

users = []
print(f"\nusers = {users}")


if users:
    for user in users:
        if user == "admin":
            print(f"Hello, {user}. Would you like to see a status report?")
        else:
            print(f"Hello {user}, thanks for logging in.")
else:
    print("We need to find more users!")