name_prompt = "\nNom? "
place_prompt = "Quel lieu visiteriez vous? "
continue_prompt = "\nVoulez-vous qu'une autre personne réponde? (y/n) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'y':
        break

print("\n--- Resultats ---")
for name, place in responses.items():
    print(f"{name.title()} aimerais visiter {place.title()}.")