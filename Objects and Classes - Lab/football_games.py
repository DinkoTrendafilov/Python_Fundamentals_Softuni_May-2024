import random

number_of_games = int(input("Enter number of games: "))

first_team_points = 0
second_team_points = 0
results_list = []

first_team_wins = 0
first_team_draws = 0
first_team_losses = 0

second_team_wins = 0
second_team_draws = 0
second_team_losses = 0

total_first_team_goals = 0
total_second_team_goals = 0

for game in range(1, number_of_games + 1):

    first_team_goals = 0
    second_team_goals = 0

    first_team_random_goals = random.randint(1, 100)
    second_team_random_goals = random.randint(1, 100)

    if first_team_random_goals in range(1, 51):
        first_team_goals = 1
    elif first_team_random_goals in range(51, 81):
        first_team_goals = 0
    elif first_team_random_goals in range(81, 91):
        first_team_goals = 2
    elif first_team_random_goals in range(91, 96):
        first_team_goals = 3
    elif first_team_random_goals in range(96, 101):
        first_team_goals = 4


    if second_team_random_goals in range(1, 51):
        second_team_goals = 1
    elif second_team_random_goals in range(51, 81):
        second_team_goals = 0
    elif second_team_random_goals in range(81, 91):
        second_team_goals = 2
    elif second_team_random_goals in range(91, 96):
        second_team_goals = 3
    elif second_team_random_goals in range(96, 101):
        second_team_goals = 4


    if first_team_goals > second_team_goals:
        first_team_points += 3
        first_team_wins += 1
        second_team_losses += 1
    elif first_team_goals < second_team_goals:
        second_team_points += 3
        second_team_wins += 1
        first_team_losses += 1
    else:
        first_team_points += 1
        second_team_points += 1
        first_team_draws += 1
        second_team_draws += 1

    res = f"{first_team_goals}:{second_team_goals}"
    results_list.append(res)
    total_first_team_goals += first_team_goals
    total_second_team_goals += second_team_goals

dictionary = {}

for item in results_list:
    if item not in dictionary:
        dictionary[item] = 1
    else:
        dictionary[item] += 1

dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1])))

for key, value in dictionary.items():
    print(f"{key} -> {value} times")


print()
print(f"First team points:{first_team_points}    Goals: {total_first_team_goals}-{total_second_team_goals} "
      f"      Wins:{first_team_wins} - Draws:{first_team_draws} - Loses:{first_team_losses}")
print(f"Second team points:{second_team_points}    Goals: {total_second_team_goals}-{total_first_team_goals}"
      f"      Wins:{second_team_wins} - Draws:{second_team_draws} - Loses:{second_team_losses}")

print()
print(f"Average goals per one match is: {((total_first_team_goals + total_second_team_goals) 
                                          / number_of_games):.2f} goals")