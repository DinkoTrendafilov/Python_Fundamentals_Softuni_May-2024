words = input().split()
dictionary = dict()

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 1
    else:
        dictionary[word_lower] += 1

for key, value in dictionary.items():
    if value % 2 == 1:
        print(key, end=" ")
