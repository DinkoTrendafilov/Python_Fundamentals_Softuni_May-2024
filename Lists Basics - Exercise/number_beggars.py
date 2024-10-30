money_list = [int(num) for num in input().split(", ")]
number_beggars = int(input())

final_money = [0] * number_beggars


for index, value in enumerate(money_list):
    final_money[index % number_beggars] += value

print(final_money)
