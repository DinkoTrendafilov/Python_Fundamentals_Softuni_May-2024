n = int(input())

collection = {}
for _ in range(n):
    piece_info = input().split("|")
    piece = piece_info[0]
    composer = piece_info[1]
    key = piece_info[2]
    collection[piece] = {"composer": composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break
    split_command = command.split("|")
    action = split_command[0]

    if action == "Add":
        piece = split_command[1]
        composer = split_command[2]
        key = split_command[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")

        else:
            print(f"{piece} by {composer} in {key} added to the collection!")
            collection[piece] = {"composer": composer, "key": key}
    elif action == "Remove":
        piece = split_command[1]
        if piece in collection:
            print(f"Successfully removed {piece}!")
            del collection[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = split_command[1]
        new_key = split_command[2]
        if piece in collection:
            collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
