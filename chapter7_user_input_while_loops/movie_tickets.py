prompt = "Age?"
prompt += "\nEntrez 'quit' quand vous avez terminé: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  Gratuit!")
    elif age < 13:
        print("  Cout: $10.")
    else:
        print(" Cout: $15.")