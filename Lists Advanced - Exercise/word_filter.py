words = input().split()

for word in words:
    result = len(word)
    if result % 2 == 0:
        print(word)
