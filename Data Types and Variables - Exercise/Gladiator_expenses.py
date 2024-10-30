number_of_lost_games = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet = number_of_lost_games // 2
total_sword = number_of_lost_games // 3
total_shield = number_of_lost_games // (2 * 3)
total_armor = total_shield // 2

expenses = total_helmet * helmet_price
expenses += total_sword * sword_price
expenses += total_shield * shield_price
expenses += total_armor * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
