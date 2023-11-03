def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nA quell album pensez-vous? "
artist_prompt = "Qui est l'artiste? "

# Let the user know how to quit.
print("Encodez 'quit' pour quitter.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nMerci de votre réponse.")