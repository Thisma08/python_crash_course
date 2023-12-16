print("Entrez deux nombres à diviser..")
print("Tapez 'q' pour quitter.")

while True:
    first_number = input("\nPremier nombre: ")
    if first_number == 'q':
        break
    second_number = input("Second nombre: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Division par 0 impossible.")
    else:
        print(answer)