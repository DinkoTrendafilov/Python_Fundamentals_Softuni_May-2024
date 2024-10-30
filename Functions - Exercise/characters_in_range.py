def character_in_range(symbol1: str, symbol2: str) -> str:
    for symbol in range(ord(symbol1) + 1, ord(symbol2)):
        print(chr(symbol), end=" ")


char_one = input()
char_two = input()

character_in_range(char_one, char_two)
