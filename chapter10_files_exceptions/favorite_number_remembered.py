from pathlib import Path
import json

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("Votre nombre favori? ")
    contents = json.dumps(number)
    path.write_text(contents)
else:
    number = json.loads(contents)
    print(f"Votre nombre favori est {number}.")