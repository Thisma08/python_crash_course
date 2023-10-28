favorite_languages = {
    'jon': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

persons = ['jon', 'mathis', 'edward', 'alice']

for name in persons:
    if name not in favorite_languages.keys():
        print(f"You should take the poll, {name.title()}!")
    else:
        print(f"Thank you for taking the poll, {name.title()}.")

