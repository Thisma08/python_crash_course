languages = ["Japanese", "French", "Dutch", "English"]

print(f"Length of the list: {len(languages)}")

print(f"List in alphabetical order: {sorted(languages)}")
print(f"List in reverse alphabetical order: {sorted(languages, reverse=True)}")

languages.sort()
print(f"List after being sorted: {languages}")

languages.pop()
print(f"List after the \"pop()\" method: {languages}")

languages.remove("Dutch")
print(f"List after the \"remove(\"Dutch\")\" method: {languages}")

del languages[0]
print(f"List after \"del languages[0]\": {languages}")

languages.insert(0, "Chinese")
print(f"List after the \"insert(0, \"Chinese\")\" method: {languages}")

languages.append("Klingon")
print(f"List after the \"append(\"Klingon\")\" method: {languages}")



