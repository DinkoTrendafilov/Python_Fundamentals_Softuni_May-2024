cards = input().split()
number_of_rotate = int(input())

for shuffle in range(number_of_rotate):
    middle = len(cards) // 2
    left_part_cards = cards[:middle]
    right_part_cards = cards[middle:]
    cards_after_shuffle = []
    for cards_index in range(len(left_part_cards)):
        cards_after_shuffle.append(left_part_cards[cards_index])
        cards_after_shuffle.append(right_part_cards[cards_index])

    cards = cards_after_shuffle
print(*cards, sep="-")
