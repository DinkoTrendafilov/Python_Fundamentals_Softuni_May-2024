cards = [number for number in input().split()]
number_of_movies = 0

while True:
    command = input()

    if command == "end":
        print(f"Sorry you lose :(")
        print(*cards)
        break
    split_command = command.split()
    first_index = int(split_command[0])
    second_index = int(split_command[1])

    number_of_movies += 1

    if first_index in range(len(cards)) and second_index in range(len(cards)) and first_index != second_index:
        el_1 = cards[first_index]
        el_2 = cards[second_index]
        if el_1 == el_2:
            cards.remove(el_1)
            cards.remove(el_2)
            print(f"Congrats! You have found matching elements - {el_1}!")
        else:
            print("Try again!")

    else:
        element_to_add = f"-{number_of_movies}a"
        middle = (len(cards) // 2)
        cards.insert(middle, element_to_add)
        cards.insert(middle, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    if len(cards) == 0:
        print(f"You have won in {number_of_movies} turns!")
        break
