import random

number_of_iteration = int(input("Enter number of iterations: "))
print()
thirds_place_points = []
team1_points = 0
team2_points = 0
team3_points = 0
team4_points = 0
winners = []
for _ in range(number_of_iteration):

    dictionary_keys = ["first_team", "second_team", "third_team", "fourth_team"]
    dictionary_values = [0 for items in range((len(dictionary_keys)))]
    dictionary = dict(zip(dictionary_keys, dictionary_values))

    result_1_match = random.randint(1, 10)
    if result_1_match in range(1, 6):
        dictionary["first_team"] += 3
        team1_points += 3

    elif result_1_match in range(6, 9):
        dictionary["first_team"] += 1
        dictionary["second_team"] += 1
        team1_points += 1
        team2_points += 1

    else:
        dictionary["second_team"] += 3
        team2_points += 3

    result_2_match = random.randint(1, 3)
    if result_2_match == 1:
        dictionary["third_team"] += 3
        team3_points += 3

    elif result_2_match == 2:
        dictionary["third_team"] += 1
        dictionary["fourth_team"] += 1
        team3_points += 1
        team4_points += 1

    else:
        dictionary["fourth_team"] += 3
        team4_points += 3

    result_3_match = random.randint(1, 10)
    if result_3_match in range(1, 6):
        dictionary["first_team"] += 3
        team1_points += 3

    elif result_3_match in range(6, 9):
        dictionary["first_team"] += 1
        dictionary["third_team"] += 1
        team1_points += 1
        team3_points += 1

    else:
        dictionary["third_team"] += 3
        team3_points += 3

    result_4_match = random.randint(1, 10)
    if result_4_match in range(1, 6):
        dictionary["second_team"] += 3
        team2_points += 3

    elif result_4_match in range(6, 9):
        dictionary["fourth_team"] += 1
        dictionary["second_team"] += 1
        team2_points += 1
        team4_points += 1

    else:
        dictionary["fourth_team"] += 3
        team4_points += 3

    result_5_match = random.randint(1, 10)
    if result_5_match in range(1, 6):
        dictionary["first_team"] += 3
        team1_points += 3

    elif result_5_match in range(6, 9):
        dictionary["first_team"] += 1
        dictionary["fourth_team"] += 1
        team1_points += 1
        team4_points += 1

    else:
        dictionary["fourth_team"] += 3
        team4_points += 3

    result_6_match = random.randint(1, 10)
    if result_6_match in range(1, 6):
        dictionary["second_team"] += 3
        team2_points += 3

    elif result_6_match in range(6, 9):
        dictionary["third_team"] += 1
        dictionary["second_team"] += 1
        team2_points += 1
        team3_points += 1

    else:
        dictionary["third_team"] += 3
        team3_points += 3

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

    result = 0
    counter = 0
    res = []
    res1 = ""

    for key, value in sorted_dictionary.items():
        counter += 1
        print(f"{key} -> {value}")
        if counter == 3:
            result = sorted_dictionary[key]
            thirds_place_points.append(result)
        res.append(key)
        res1 = "-".join(map(str, res))
    winners.append(res1)

    print()

third_places_dictionary = {}

for el in thirds_place_points:
    if el not in third_places_dictionary:
        third_places_dictionary[el] = 1
    else:
        third_places_dictionary[el] += 1

sorted_third_places_dictionary = dict(sorted(third_places_dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

for key, value in sorted_third_places_dictionary.items():
    result_as_percent = value / number_of_iteration * 100
    print(f"Third place: {key} points -> Times happened: {value} = {result_as_percent:.2f} %")
print()
print(
    f"Average points -> team1: {(team1_points / number_of_iteration):.2f} hcp, "
    f"team2: {(team2_points / number_of_iteration):.2f} hcp, "
    f"team3: {(team3_points / number_of_iteration):.2f} hcp, "
    f"team4: {(team4_points / number_of_iteration):.2f} hcp")
print()

statistic_dictionary = {}

for el in winners:
    if el not in statistic_dictionary:
        statistic_dictionary[el] = 1
    else:
        statistic_dictionary[el] += 1

sorted_statistic_dictionary = dict(sorted(statistic_dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

for key, value in sorted_statistic_dictionary.items():
    print(f"{key} -> {value} = {((value / number_of_iteration) * 100):.2f} %")


