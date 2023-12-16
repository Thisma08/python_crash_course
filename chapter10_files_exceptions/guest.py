from pathlib import Path

path = Path('guest.txt')

name = input("Votre nom? ")
path.write_text(name)