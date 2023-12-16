filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError as e:
    msg = "Le fichier " + filename + " n'existe pas."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("La fichier " + filename + " contient " + str(num_words) + " mots.")