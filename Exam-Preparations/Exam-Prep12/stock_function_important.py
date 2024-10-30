percent_profit = float(input("Enter your % profit: "))
numbers_of_years = int(input("Enter years: "))

res = ((percent_profit / 100) + 1)
result = res ** (1 / numbers_of_years)
result_as_percent = (result * 100) - 100

print()
print(f"Your up is 1 to {res:.2f}")
print(f"Your profit {percent_profit} % for {numbers_of_years} years  =  {result_as_percent:.2f} % per year up.")
