while True:
    word = input()
    if word == 'end':
        break
    rev_word = word[::-1]
    print(f"{word} = {rev_word}")
