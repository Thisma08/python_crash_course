glossary = {
    'for': 'Creates a "for" loop (Known amount of iterations)',
    'while': 'Creates a "while" loop (Unknown amount of iterations)',
    'print': 'Prints a statement or the value of a variable',
    'in': 'Used to loop through the elements of a list (To use with a "for" loop)',
    'sort()': 'Sorts a list',
    'reverse()': 'Reverses the order of a list'
}

for term, meaning in glossary.items():
    print(f"{term}: {meaning}")
