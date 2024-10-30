countries = input().split(", ")
capitals = input().split(", ")

dictionary = dict(zip(countries, capitals))

for key, values in dictionary.items():
    print(f"{key} -> {values}")