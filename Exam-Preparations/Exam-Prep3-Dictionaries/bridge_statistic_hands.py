import random

n = int(input("Enter number of iterations: "))
ended_dictionary = {}
total_points = 0
total_distribution = []

void_spades = 0
void_hearts = 0
void_diamonds = 0
void_clubs = 0

distribution_4_3_3_3 = 0
distribution_4_4_3_2 = 0
distribution_5_3_3_2 = 0
distribution_5_4_2_2 = 0
distribution_4_4_4_1 = 0
distribution_5_4_3_1 = 0
distribution_dictionary = {}
for _ in range(n):
    dictionary = {"Spades": 0, "Hearts": 0, "Diamonds": 0, "Clubs": 0}
    cards_in_hand = []
    points = 0

    for _ in range(1000):
        random_card = random.randint(1, 52)

        if random_card not in cards_in_hand:
            cards_in_hand.append(random_card)
        if len(cards_in_hand) == 13:
            break

    for card in cards_in_hand:
        if card in range(1, 14):
            suit = "Clubs"
            if suit not in dictionary:
                dictionary[suit] = 1
            else:
                dictionary[suit] += 1
        elif card in range(14, 27):
            suit = "Diamonds"
            if suit not in dictionary:
                dictionary[suit] = 1
            else:
                dictionary[suit] += 1
        elif card in range(27, 40):
            suit = "Hearts"
            if suit not in dictionary:
                dictionary[suit] = 1
            else:
                dictionary[suit] += 1
        else:
            suit = "Spades"
            if suit not in dictionary:
                dictionary[suit] = 1
            else:
                dictionary[suit] += 1

    for card in cards_in_hand:
        if card in (1, 14, 27, 40):
            points += 4
        elif card in (11, 24, 37, 50):
            points += 1
        elif card in (12, 25, 38, 51):
            points += 2
        elif card in (13, 26, 39, 52):
            points += 3

    total_points += points

    a = []
    for (key, value) in dictionary.items():
        a.append(value)
    total_distribution.append(a)

total_spade_cards = 0
total_heard_cards = 0
total_diamond_cards = 0
total_clubs_cards = 0

for el in total_distribution:
    if el[0] == 0:
        void_spades += 1
    if el[1] == 0:
        void_hearts += 1
    if el[2] == 0:
        void_diamonds += 1
    if el[3] == 0:
        void_clubs += 1
    total_spade_cards += el[0]
    total_heard_cards += el[1]
    total_diamond_cards += el[2]
    total_clubs_cards += el[3]
    if tuple(el) not in ended_dictionary:
        ended_dictionary[tuple(el)] = 1
    else:
        ended_dictionary[tuple(el)] += 1

sorted_dictionary = dict(sorted(ended_dictionary.items(), key=lambda kv: (-kv[1], -kv[0][0],
                                                                          -kv[0][1], -kv[0][2], -kv[0][3])))

max_key = 0
max_value = max(sorted_dictionary.values())
counter = 0
for (key, value) in sorted_dictionary.items():
    counter += 1
    if counter in (1, 2, 3, 4):
        distribution_4_3_3_3 += value
    elif counter in range(5, 17):
        distribution_4_4_3_2 += value
    elif counter in range(17, 29):
        distribution_5_3_3_2 += value
    elif counter in range(29, 41):
        distribution_5_4_2_2 += value
    elif counter in (41, 42, 43, 44):
        distribution_4_4_4_1 += value
    elif counter in range(45, 69):
        distribution_5_4_3_1 += value

    if value == max_value:
        max_key = key
    print(f"{counter}: {key} -> {value:_} --> {(value / n * 100):.2f} %")

print()
print(f"Total spade cards: {total_spade_cards:_} - Average cards: {(total_spade_cards / n):.2f}")
print(f"Total heard cards: {total_heard_cards:_} - Average cards: {(total_heard_cards / n):.2f}")
print(f"Total diamond cards: {total_diamond_cards:_} - Average cards: {(total_diamond_cards / n):.2f}")
print(f"Total clubs cards: {total_clubs_cards:_} - Average cards: {(total_clubs_cards / n):.2f}")
print()
print()
print(f"The best combination is: {max_key} with {max_value:_} times.")
print(f"Total points: {total_points:_}")
print(f"Average points: {(total_points / n):.2f}")
print()
print(len(sorted_dictionary))
print()
print(f"Spades voids is: {void_spades:_} --> {(void_spades / n * 100):.2f} %")
print(f"Hearts voids is: {void_hearts:_} --> {(void_hearts / n * 100):.2f} %")
print(f"Diamonds voids is: {void_diamonds:_} --> {(void_diamonds / n * 100):.2f} %")
print(f"Clubs voids is: {void_clubs:_} --> {(void_clubs / n * 100):.2f} %")
print(f"Total Voids: {((void_clubs + void_diamonds + void_hearts + void_spades) / n * 100):.2f} %")
print()
print()

print(f"4-4-3-2 distribution: {distribution_4_4_3_2:_} times --> {(distribution_4_4_3_2 / n * 100):.2f} %")
print(f"5-3-3-2 distribution: {distribution_5_3_3_2:_} times --> {(distribution_5_3_3_2 / n * 100):.2f} %")
print(f"5-4-3-1 distribution: {distribution_5_4_3_1:_} times --> {(distribution_5_4_3_1 / n * 100):.2f} %")
print(f"5-4-2-2 distribution: {distribution_5_4_2_2:_} times --> {(distribution_5_4_2_2 / n * 100):.2f} %")
print(f"4-3-3-3 distribution: {distribution_4_3_3_3:_} times --> {(distribution_4_3_3_3 / n * 100):.2f} %")
print(f"4-4-4-1 distribution: {distribution_4_4_4_1:_} times --> {(distribution_4_4_4_1 / n * 100):.2f} %")
print()
print(f"4-4-3-2 distribution: {(distribution_4_4_3_2 / n * 100):.2f} %")
print(f"5-3-3-2 distribution: {(distribution_5_3_3_2 / n * 100):.2f} %")
print(f"5-4-3-1 distribution: {(distribution_5_4_3_1 / n * 100):.2f} %")
print(f"5-4-2-2 distribution: {(distribution_5_4_2_2 / n * 100):.2f} %")
print(f"4-3-3-3 distribution: {(distribution_4_3_3_3 / n * 100):.2f} %")
print(f"4-4-4-1 distribution: {(distribution_4_4_4_1 / n * 100):.2f} %")
