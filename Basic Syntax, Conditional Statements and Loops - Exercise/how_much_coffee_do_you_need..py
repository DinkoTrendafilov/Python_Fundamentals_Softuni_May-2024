needed_coffee = 0

while True:
    command = input()
    if command == "END":
        break
    if command in ("movie", "dog", "cat", "coding"):
        needed_coffee += 1
    elif command in ("MOVIE", "DOG", "CAT", "CODING"):
        needed_coffee += 2

if needed_coffee <= 5:
    print(needed_coffee)
else:
    print("You need extra sleep")
