import random

matches_count = int(input("Enter number of matches: "))
iterations_count = int(input("Enter number of iterations: "))
needed_percent = int(input("Enter needed % : "))

total_result_player = []
dictionary = {}
lucky_combination = []
match_number_combination = []

for iteration in range(iterations_count):
    pc_prognosis = []
    player_prognosis = []
    result_player = 0

    for _ in range(matches_count):
        random_number_pc = random.randint(1, 3)
        if random_number_pc == 1:
            pc_prognosis.append("1")
        elif random_number_pc == 2:
            pc_prognosis.append("2")
        else:
            pc_prognosis.append("x")

        random_number_player = random.randint(1, 3)
        if random_number_player == 1:
            player_prognosis.append("1")
        elif random_number_player == 2:
            player_prognosis.append("2")
        else:
            player_prognosis.append("x")

    for i in range(len(pc_prognosis)):
        if pc_prognosis[i] == player_prognosis[i]:
            result_player += 1
        if result_player == matches_count:
            match_number_combination.append(iteration + 1)
            lucky_combination.append(player_prognosis)

    total_result_player.append(result_player)

for el in total_result_player:
    if el not in dictionary:
        dictionary[el] = 1
    else:
        dictionary[el] += 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

print()
for (key, value) in sorted_dictionary.items():
    print(f"Result: {key} -> Times: {value:_} -> {(value / iterations_count * 100):.2f} %")

print()
print(f"Total numbers of combination of {matches_count} matches is: {(3 ** matches_count):_}")
print(f"Your number of iteration: {iterations_count:_} is "
      f"{((iterations_count / (3 ** matches_count)) * 100):.2f} % from total combinations.")

print()
for i in range(len(lucky_combination)):
    print(
        f"# {i + 1}: Lucky combination: {', '.join(lucky_combination[i])}"
        f" -> Combination number: # {match_number_combination[i]:_}")

print()
print(f"Count of lucky combinations: {len(lucky_combination):_}")
print(f"Needed Average combination: {(iterations_count / 3 ** matches_count):.2f}")
if len(lucky_combination) >= (iterations_count / 3 ** matches_count):
    print(f"Congratulation!!!  You have a good result: {len(lucky_combination):_}")
else:
    print("You failed, so sorry :(")
print()

needed_number = int(len(sorted_dictionary) * needed_percent / 100)
counter = 0
total_value = 0
for (key, value) in sorted_dictionary.items():
    counter += 1
    if counter in range(1, needed_number + 1):
        print(f"Key: {key} --> Value: {value:_}")
        total_value += value
print()
print(f"Top: {needed_percent} %  makes: {((total_value / iterations_count) * 100):.2f} %")
print()
print(f"Matches count: {matches_count}")
print(f"Count of elements: {len(sorted_dictionary)}")
print(f"Needed %: {needed_percent}")
print(f"Needed number: {needed_number}")
print()
