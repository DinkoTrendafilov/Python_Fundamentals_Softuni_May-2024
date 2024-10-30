some_string = input()
final_string = ""
last_added_character = ""

for current_character in some_string:
    if current_character != last_added_character:
        final_string += current_character
        last_added_character = current_character

print(final_string)
