import random

# home wins as default = 60%,  draw result as default = 30% , away wins as default = 10%
number_of_games = int(input("Enter number of games: "))
results_dictionary = {}

for i in range(13, -1, -1):
    for j in range(13, -1, -1):
        for k in range(13, -1, -1):
            result = i + j + k
            if result == 13:
                res = f"{i}-{j}-{k}"
                results_dictionary[res] = 0
full_stats = []
total_home = 0
total_draw = 0
total_away = 0
for game in range(number_of_games):
    result = ""
    home = 0
    draw = 0
    away = 0
    for _ in range(13):
        random_result = random.randint(1, 100)
        if random_result in range(1, 61):
            home += 1
            total_home += 1

        elif random_result in range(61, 91):
            draw += 1
            total_draw += 1

        else:
            away += 1
            total_away += 1

    result = f"{home}-{draw}-{away}"
    full_stats.append(result)
    print(f"Game: {game} - Result is: {result}")
print()
for item in full_stats:
    if item not in results_dictionary:
        results_dictionary[item] = 1
    else:
        results_dictionary[item] += 1

sorted_dictionary = dict(sorted(results_dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

res = 0
res_as_percent = 0
for key, value in sorted_dictionary.items():
    print(f"Key: {key} - Value: {value:02d} : {((value / number_of_games) * 100):.2f}%")

print()
total_home_as_percent = round(total_home / (total_away + total_draw + total_home) * 100, 2)
total_draw_as_percent = round(total_draw / (total_away + total_draw + total_home) * 100, 2)
total_away_as_percent = (100 - (total_home_as_percent + total_draw_as_percent))
print(f"Total Statistic: {total_home} : {total_draw} : {total_away}")
print(f"Total % : {total_home_as_percent}% : {total_draw_as_percent}% : {total_away_as_percent :.2f}%")

print(f"Max numbers of combinations are: {3 ** 13}")
