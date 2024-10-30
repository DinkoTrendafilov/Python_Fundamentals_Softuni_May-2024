initial_text = input()
encrypted_version = ""

for character in initial_text:
    encrypted_character = chr(ord(character) + 3)
    encrypted_version += encrypted_character

print(encrypted_version)



