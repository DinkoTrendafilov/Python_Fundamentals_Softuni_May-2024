import random

number_of_iterations = int(input("Enter number of iterations: "))
third_place_teams = []
third_place_teams1 = []

for _ in range(number_of_iterations):

    dictionary = {}

    dictionary["Bulgaria"] = {"points": 0, "goals_diff": 0,
                              "scored_goals": 0, "considered_goals": 0}
    dictionary["France"] = {"points": 0, "goals_diff": 0,
                            "scored_goals": 0, "considered_goals": 0}
    dictionary["Italy"] = {"points": 0, "goals_diff": 0,
                           "scored_goals": 0, "considered_goals": 0}
    dictionary["England"] = {"points": 0, "goals_diff": 0,
                             "scored_goals": 0, "considered_goals": 0}

    first_team = random.randint(1, 100)
    if first_team in range(1, 41):
        first_team_goals = 2
    elif first_team in range(41, 71):
        first_team_goals = 1
    elif first_team in range(71, 91):
        first_team_goals = 3
    else:
        first_team_goals = 0

    second_team = random.randint(1, 100)
    if second_team in range(1, 41):
        second_team_goals = 2
    elif second_team in range(41, 71):
        second_team_goals = 1
    elif second_team in range(71, 91):
        second_team_goals = 3
    else:
        second_team_goals = 0

    if first_team_goals > second_team_goals:
        dictionary["Bulgaria"]["points"] += 3
        dictionary["Bulgaria"]["goals_diff"] += first_team_goals - second_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["France"]["points"] += 0
        dictionary["France"]["goals_diff"] -= first_team_goals - second_team_goals
        dictionary["France"]["scored_goals"] += second_team_goals
        dictionary["France"]["considered_goals"] += first_team_goals
    elif second_team_goals > first_team_goals:
        dictionary["Bulgaria"]["points"] += 0
        dictionary["Bulgaria"]["goals_diff"] -= second_team_goals - first_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["France"]["points"] += 3
        dictionary["France"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["France"]["scored_goals"] += second_team_goals
        dictionary["France"]["considered_goals"] += first_team_goals

    else:
        dictionary["Bulgaria"]["points"] += 1
        dictionary["Bulgaria"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["France"]["points"] += 1
        dictionary["France"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["France"]["scored_goals"] += second_team_goals
        dictionary["France"]["considered_goals"] += first_team_goals

    third_team = random.randint(1, 100)
    if third_team in range(1, 41):
        third_team_goals = 2
    elif third_team in range(41, 71):
        third_team_goals = 1
    elif third_team in range(71, 91):
        third_team_goals = 3
    else:
        third_team_goals = 0

    fourth_team = random.randint(1, 100)
    if fourth_team in range(1, 41):
        fourth_team_goals = 2
    elif fourth_team in range(41, 71):
        fourth_team_goals = 1
    elif fourth_team in range(71, 91):
        fourth_team_goals = 3
    else:
        fourth_team_goals = 0

    if third_team_goals > fourth_team_goals:
        dictionary["Italy"]["points"] += 3
        dictionary["Italy"]["goals_diff"] += third_team_goals - fourth_team_goals
        dictionary["Italy"]["scored_goals"] += third_team_goals
        dictionary["Italy"]["considered_goals"] += fourth_team_goals

        dictionary["England"]["points"] += 0
        dictionary["England"]["goals_diff"] -= third_team_goals - fourth_team_goals
        dictionary["England"]["scored_goals"] += fourth_team_goals
        dictionary["England"]["considered_goals"] += third_team_goals

    elif fourth_team_goals > third_team_goals:
        dictionary["Italy"]["points"] += 0
        dictionary["Italy"]["goals_diff"] -= fourth_team_goals - third_team_goals
        dictionary["Italy"]["scored_goals"] += third_team_goals
        dictionary["Italy"]["considered_goals"] += fourth_team_goals

        dictionary["England"]["points"] += 3
        dictionary["England"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["England"]["scored_goals"] += fourth_team_goals
        dictionary["England"]["considered_goals"] += third_team_goals

    else:
        dictionary["Italy"]["points"] += 1
        dictionary["Italy"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["Italy"]["scored_goals"] += third_team_goals
        dictionary["Italy"]["considered_goals"] += fourth_team_goals

        dictionary["England"]["points"] += 1
        dictionary["England"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["England"]["scored_goals"] += fourth_team_goals
        dictionary["England"]["considered_goals"] += third_team_goals

    first_team = random.randint(1, 100)
    if first_team in range(1, 41):
        first_team_goals = 2
    elif first_team in range(41, 71):
        first_team_goals = 1
    elif first_team in range(71, 91):
        first_team_goals = 3
    else:
        first_team_goals = 0

    second_team = random.randint(1, 100)
    if second_team in range(1, 41):
        second_team_goals = 2
    elif second_team in range(41, 71):
        second_team_goals = 1
    elif second_team in range(71, 91):
        second_team_goals = 3
    else:
        second_team_goals = 0

    if first_team_goals > second_team_goals:
        dictionary["Bulgaria"]["points"] += 3
        dictionary["Bulgaria"]["goals_diff"] += first_team_goals - second_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["Italy"]["points"] += 0
        dictionary["Italy"]["goals_diff"] -= first_team_goals - second_team_goals
        dictionary["Italy"]["scored_goals"] += second_team_goals
        dictionary["Italy"]["considered_goals"] += first_team_goals
    elif second_team_goals > first_team_goals:
        dictionary["Bulgaria"]["points"] += 0
        dictionary["Bulgaria"]["goals_diff"] -= second_team_goals - first_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["Italy"]["points"] += 3
        dictionary["Italy"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["Italy"]["scored_goals"] += second_team_goals
        dictionary["Italy"]["considered_goals"] += first_team_goals

    else:
        dictionary["Bulgaria"]["points"] += 1
        dictionary["Bulgaria"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["Italy"]["points"] += 1
        dictionary["Italy"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["Italy"]["scored_goals"] += second_team_goals
        dictionary["Italy"]["considered_goals"] += first_team_goals

    third_team = random.randint(1, 100)
    if third_team in range(1, 41):
        third_team_goals = 2
    elif third_team in range(41, 71):
        third_team_goals = 1
    elif third_team in range(71, 91):
        third_team_goals = 3
    else:
        third_team_goals = 0

    fourth_team = random.randint(1, 100)
    if fourth_team in range(1, 41):
        fourth_team_goals = 2
    elif fourth_team in range(41, 71):
        fourth_team_goals = 1
    elif fourth_team in range(71, 91):
        fourth_team_goals = 3
    else:
        fourth_team_goals = 0

    if third_team_goals > fourth_team_goals:
        dictionary["France"]["points"] += 3
        dictionary["France"]["goals_diff"] += third_team_goals - fourth_team_goals
        dictionary["France"]["scored_goals"] += third_team_goals
        dictionary["France"]["considered_goals"] += fourth_team_goals

        dictionary["England"]["points"] += 0
        dictionary["England"]["goals_diff"] -= third_team_goals - fourth_team_goals
        dictionary["England"]["scored_goals"] += fourth_team_goals
        dictionary["England"]["considered_goals"] += third_team_goals

    elif fourth_team_goals > third_team_goals:
        dictionary["France"]["points"] += 0
        dictionary["France"]["goals_diff"] -= fourth_team_goals - third_team_goals
        dictionary["France"]["scored_goals"] += third_team_goals
        dictionary["France"]["considered_goals"] += fourth_team_goals

        dictionary["England"]["points"] += 3
        dictionary["England"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["England"]["scored_goals"] += fourth_team_goals
        dictionary["England"]["considered_goals"] += third_team_goals

    else:
        dictionary["France"]["points"] += 1
        dictionary["France"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["France"]["scored_goals"] += third_team_goals
        dictionary["France"]["considered_goals"] += fourth_team_goals

        dictionary["England"]["points"] += 1
        dictionary["England"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["England"]["scored_goals"] += fourth_team_goals
        dictionary["England"]["considered_goals"] += third_team_goals

    first_team = random.randint(1, 100)
    if first_team in range(1, 41):
        first_team_goals = 2
    elif first_team in range(41, 71):
        first_team_goals = 1
    elif first_team in range(71, 91):
        first_team_goals = 3
    else:
        first_team_goals = 0

    second_team = random.randint(1, 100)
    if second_team in range(1, 41):
        second_team_goals = 2
    elif second_team in range(41, 71):
        second_team_goals = 1
    elif second_team in range(71, 91):
        second_team_goals = 3
    else:
        second_team_goals = 0

    if first_team_goals > second_team_goals:
        dictionary["Bulgaria"]["points"] += 3
        dictionary["Bulgaria"]["goals_diff"] += first_team_goals - second_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["England"]["points"] += 0
        dictionary["England"]["goals_diff"] -= first_team_goals - second_team_goals
        dictionary["England"]["scored_goals"] += second_team_goals
        dictionary["England"]["considered_goals"] += first_team_goals
    elif second_team_goals > first_team_goals:
        dictionary["Bulgaria"]["points"] += 0
        dictionary["Bulgaria"]["goals_diff"] -= second_team_goals - first_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["England"]["points"] += 3
        dictionary["England"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["England"]["scored_goals"] += second_team_goals
        dictionary["England"]["considered_goals"] += first_team_goals

    else:
        dictionary["Bulgaria"]["points"] += 1
        dictionary["Bulgaria"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["Bulgaria"]["scored_goals"] += first_team_goals
        dictionary["Bulgaria"]["considered_goals"] += second_team_goals

        dictionary["England"]["points"] += 1
        dictionary["England"]["goals_diff"] += second_team_goals - first_team_goals
        dictionary["England"]["scored_goals"] += second_team_goals
        dictionary["England"]["considered_goals"] += first_team_goals

    third_team = random.randint(1, 100)
    if third_team in range(1, 41):
        third_team_goals = 2
    elif third_team in range(41, 71):
        third_team_goals = 1
    elif third_team in range(71, 91):
        third_team_goals = 3
    else:
        third_team_goals = 0

    fourth_team = random.randint(1, 100)
    if fourth_team in range(1, 41):
        fourth_team_goals = 2
    elif fourth_team in range(41, 71):
        fourth_team_goals = 1
    elif fourth_team in range(71, 91):
        fourth_team_goals = 3
    else:
        fourth_team_goals = 0

    if third_team_goals > fourth_team_goals:
        dictionary["France"]["points"] += 3
        dictionary["France"]["goals_diff"] += third_team_goals - fourth_team_goals
        dictionary["France"]["scored_goals"] += third_team_goals
        dictionary["France"]["considered_goals"] += fourth_team_goals

        dictionary["Italy"]["points"] += 0
        dictionary["Italy"]["goals_diff"] -= third_team_goals - fourth_team_goals
        dictionary["Italy"]["scored_goals"] += fourth_team_goals
        dictionary["Italy"]["considered_goals"] += third_team_goals

    elif fourth_team_goals > third_team_goals:
        dictionary["France"]["points"] += 0
        dictionary["France"]["goals_diff"] -= fourth_team_goals - third_team_goals
        dictionary["France"]["scored_goals"] += third_team_goals
        dictionary["France"]["considered_goals"] += fourth_team_goals

        dictionary["Italy"]["points"] += 3
        dictionary["Italy"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["Italy"]["scored_goals"] += fourth_team_goals
        dictionary["Italy"]["considered_goals"] += third_team_goals

    else:
        dictionary["France"]["points"] += 1
        dictionary["France"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["France"]["scored_goals"] += third_team_goals
        dictionary["France"]["considered_goals"] += fourth_team_goals

        dictionary["Italy"]["points"] += 1
        dictionary["Italy"]["goals_diff"] += fourth_team_goals - third_team_goals
        dictionary["Italy"]["scored_goals"] += fourth_team_goals
        dictionary["Italy"]["considered_goals"] += third_team_goals

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1]["points"],
                                                                        -kv[1]["goals_diff"],
                                                                        -kv[1]["scored_goals"],
                                                                        -kv[1]["considered_goals"])))
    third_place_counter = 0
    for (key, value) in sorted_dictionary.items():
        third_place_counter += 1
        if third_place_counter == 3:
            third_place_teams1.append([value['points'], value['goals_diff']])

            third_place_teams.append(f"{value['points']} points, {value['goals_diff']} goals_diff, "
                                     f", {value['scored_goals']} scored_goals, {value['considered_goals']} considered_goals")

# for item in third_place_teams:
#     print(item)
#
# print()
# print()
sorted_third_place_teams1 = list(sorted(third_place_teams1, key=lambda item: (-item[0], -item[1])))
counter = 0
for item in sorted_third_place_teams1:
    counter += 1
    print(f"#: {counter:_} - pts: {item[0]} - goals_diff: {item[1]}")
