prompt = "\nQuel topping voulez vous sur votre pizza?"
prompt += "\nEntre 'quit' quand vous avez terminé: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  Ajout de {topping} sur la pizza.")
    else:
        break