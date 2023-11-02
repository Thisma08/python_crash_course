def make_shirt(size='large', message = 'J\'aime Python!'):
    print(f"\nJe vais faire un t-shirt de taille {size}.")
    print(f'Il dira: "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'La lisibilité compte.')