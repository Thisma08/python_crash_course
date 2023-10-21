users = ["Mathis", "Alice", "Sam", "admin", "Claire", "Marc"]

for user in users:
    if user == "admin":
        print(f"Hello, {user}. Would you like to see a status report?")
    else:
        print(f"Hello {user}, thanks for logging in.")