from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nVotre nom ? "
prompt += "\nTapez 'q' pour finir. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'q':
        break

    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)