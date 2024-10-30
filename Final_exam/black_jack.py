import random

n = int(input("Enter number of iterations: "))
win = 0
lose = 0
draw = 0
total_player_points = []
total_21_player_points = 0
total_0_player_points = 0
total_pc_points = []
total_21_pc_points = 0
total_0_pc_points = 0

for _ in range(n):
    pc_points = 0
    player_points = 0

    # Генериране на случайни числа за PC
    first_random_number_pc = random.randint(1, 52)
    second_random_number_pc = random.randint(1, 52)
    third_random_number_pc = random.randint(1, 52)
    fourth_random_number_pc = random.randint(1, 52)
    five_random_number_pc = random.randint(1, 52)
    six_random_number_pc = random.randint(1, 52)
    seven_random_number_pc = random.randint(1, 52)

    # Генериране на случайни числа за играча
    first_random_number_player = random.randint(1, 52)
    second_random_number_player = random.randint(1, 52)
    third_random_number_player = random.randint(1, 52)
    fourth_random_number_player = random.randint(1, 52)
    five_random_number_player = random.randint(1, 52)
    six_random_number_player = random.randint(1, 52)
    seven_random_number_player = random.randint(1, 52)

    # Пресмятане на точките за PC
    for random_number_pc in [first_random_number_pc, second_random_number_pc, third_random_number_pc,
                             fourth_random_number_pc, five_random_number_pc,
                             six_random_number_pc, seven_random_number_pc]:
        if random_number_pc in (1, 14, 27, 40):
            pc_points += 11
        elif random_number_pc in (11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52):
            pc_points += 10
        elif random_number_pc in (2, 15, 28, 41):
            pc_points += 2
        elif random_number_pc in (3, 16, 29, 42):
            pc_points += 3
        elif random_number_pc in (4, 17, 30, 43):
            pc_points += 4
        elif random_number_pc in (5, 18, 31, 44):
            pc_points += 5
        elif random_number_pc in (6, 19, 32, 45):
            pc_points += 6
        elif random_number_pc in (7, 20, 33, 46):
            pc_points += 7
        elif random_number_pc in (8, 21, 34, 47):
            pc_points += 8
        elif random_number_pc in (9, 22, 35, 48):
            pc_points += 9
        elif random_number_pc in (10, 23, 36, 49):
            pc_points += 10
        if pc_points >= 14:
            break

    if pc_points > 21:
        pc_points = 0
        total_0_pc_points += 1
    if pc_points == 21:
        total_21_pc_points += 1
    total_pc_points.append(pc_points)

    # Пресмятане на точките за играча
    for random_number_player in [first_random_number_player, second_random_number_player, third_random_number_player,
                                 fourth_random_number_player, five_random_number_player,
                                 six_random_number_player, seven_random_number_player]:
        if random_number_player in (1, 14, 27, 40):
            player_points += 11
        elif random_number_player in (11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52):
            player_points += 10
        elif random_number_player in (2, 15, 28, 41):
            player_points += 2
        elif random_number_player in (3, 16, 29, 42):
            player_points += 3
        elif random_number_player in (4, 17, 30, 43):
            player_points += 4
        elif random_number_player in (5, 18, 31, 44):
            player_points += 5
        elif random_number_player in (6, 19, 32, 45):
            player_points += 6
        elif random_number_player in (7, 20, 33, 46):
            player_points += 7
        elif random_number_player in (8, 21, 34, 47):
            player_points += 8
        elif random_number_player in (9, 22, 35, 48):
            player_points += 9
        elif random_number_player in (10, 23, 36, 49):
            player_points += 10
        if player_points >= 14:
            break

    if player_points > 21:
        player_points = 0
        total_0_player_points += 1

    if player_points == 21:
        total_21_player_points += 1

    total_player_points.append(player_points)

    # Определяне на резултатите
    if pc_points > player_points:
        lose += 1
    elif pc_points < player_points:
        win += 1
    else:
        draw += 1

print(f"Player result: Wins: {win:_} : Draws: {draw:_} : Loses: {lose:_}")
print()
print(f"Total Player sum result: {sum(total_player_points):_} points --> AVERAGE: {(sum(total_player_points) / n):.2f}")
print(f"Total PC sum result: {sum(total_pc_points):_} points --> AVERAGE: {(sum(total_pc_points) / n):.2f}")
print()
print(f"Diff between Wins and Loses result is: {((win / lose) * 100 - 100):.2f} %")
print()
print(f"Total 21 in player result: {total_21_player_points:_} --> {((total_21_player_points / n) * 100):.2f} %")
print(f"Total 21 in pc result: {total_21_pc_points:_} --> {((total_21_pc_points / n) * 100):.2f} %")
print()
print(f"Total 0 in player result: {total_0_player_points:_} --> {((total_0_player_points / n) * 100):.2f} %")
print(f"Total 0 in pc result: {total_0_pc_points:_} --> {((total_0_pc_points / n) * 100):.2f} %")
print()
print(f"{'-' * 100}")

dictionary_player = {}
dictionary_pc = {}

for el in total_player_points:
    if el in dictionary_player:
        dictionary_player[el] += 1
    else:
        dictionary_player[el] = 1

for el in total_pc_points:
    if el in dictionary_pc:
        dictionary_pc[el] += 1
    else:
        dictionary_pc[el] = 1

sorted_dictionary_player = dict(sorted(dictionary_player.items(), key=lambda kv: (-kv[1], kv[0])))
sorted_dictionary_pc = dict(sorted(dictionary_pc.items(), key=lambda kv: (-kv[1], kv[0])))

print(f"Player Statistic: ")
for (key, value) in sorted_dictionary_player.items():
    print(f"Number: {key:_} --> {((value / n) * 100):.2f} %")

print(f"{'-' * 100}")
print(f"Pc Statistic: ")
for (key, value) in sorted_dictionary_pc.items():
    print(f"Number: {key:_} --> {((value / n) * 100):.2f} %")
print(f"{'-' * 100}")
