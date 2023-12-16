from pathlib import Path

path = Path('programming_poll.txt')

prompt = "\nPourquoi aimez-vous programmer ? "
prompt += "\nTapez 'q' pour finir. "

while True:
    reason = input(prompt)
    if reason == 'q':
        break
        
    file_string += f"{name}\n"
    path.write_text(file_string)