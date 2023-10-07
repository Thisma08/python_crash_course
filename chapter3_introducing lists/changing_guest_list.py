guests = ["Alice", "Marc", "Claire", "Sam"]

for guest in guests:
    print(f"I'd like to invite you to dinner, {guest}!")

print(f"Oh crap, {guests[3]} can't make it...")

guests[3] = "Barack Obama"

for guest in guests:
    print(f"I'd like to invite you to dinner, {guest}!")