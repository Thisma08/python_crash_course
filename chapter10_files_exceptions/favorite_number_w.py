from pathlib import Path
import json

number = input("Votre nombre favori? ")

path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)