symbols = input().split(", ")
dictionary = dict()

for symbol in symbols:
    dictionary[symbol] = ord(symbol)

print(dictionary)
