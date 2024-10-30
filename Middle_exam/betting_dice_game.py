import random

number_of_games = int(input("Enter your number of games: "))
started_money = float(input("Enter your initial betting money: "))
money = started_money
win = 0
lost = 0

for game in range(1, number_of_games + 1):
    bet_money = float(input("Enter your betting money: "))

    if bet_money > money:
        print(f"Betting max your initial money")
        continue

    player_bet_choice = input(
        "Enter your betting choice [f = [3-10],s = [11-18],o = odd numbers in (3-18),e = even numbers in (3-18)]: ")
    win_numbers = []
    numbers = [num for num in range(3, 19)]

    if player_bet_choice == "e":
        win_numbers = [num for num in numbers if num % 2 == 0]
    elif player_bet_choice == "o":
        win_numbers = [num for num in numbers if num % 2 == 1]
    elif player_bet_choice == "f":
        win_numbers = numbers[0:len(numbers) // 2]
    elif player_bet_choice == "s":
        win_numbers = s = numbers[len(numbers) // 2:]

    money -= bet_money
    random_dice_sum = random.randint(3, 18)
    if random_dice_sum in win_numbers:
        money += bet_money * 1.8
        print(f"Congratulations! In game: {game} -  You won {bet_money * 1.8}lv.")
        print(f"Right random sum is: {random_dice_sum}")
        print(f"Your current money is: {money}")
        win += 1
        print()

    else:
        lost += 1
        print(f"Sorry, in game: {game} you lost your bet of {bet_money:.2f}lv.")
        print(f"Right random sum is: {random_dice_sum}")
        print(f"Your current money is: {money}")
        print()

    if money <= 0:
        print(f"Sorry, you lost your bet of {started_money:.2f}lv.")
        print(f"Right random sum is: {random_dice_sum}")
        print()
        break
print(f"After {number_of_games} games, =>  WINS: {win}  =>  LOSES: {lost}")
print(f"Your balance is: {money:.2f} you started with {started_money}")
res_as_string = ""
result = (money / started_money) * 100 - 100
if result >= 0:
    res_as_string = "Profit"
else:
    res_as_string = "Loss"

print(f"Your make {result:.2f} % {res_as_string}")
print()
