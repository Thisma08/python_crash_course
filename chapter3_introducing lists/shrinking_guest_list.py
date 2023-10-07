guests = ["Alice", "Marc", "Claire", "Sam"]

for guest in guests:
    print(f"I'd like to invite you to dinner, {guest}!")

print("Ayo I just found a bigger table!")

guests.insert(0, "Mario")
guests.insert(3, "Shrek")
guests.append("God")

for guest in guests:
    print(f"I'd like to invite you to dinner, {guest}!")

print("I can invite only two people...")

while(len(guests) > 2):
    guests.pop()

for guest in guests:
    print(f"{guest} is still invited.")

del guests[1]
del guests[0]

for guest in guests:
    print(guest)