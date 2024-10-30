n = int(input())

for _ in range(n):
    current_text = input()
    is_pure = True
    for symbol in current_text:
        if symbol in (",", "_", "."):
            is_pure = False
            break
    if is_pure:
        print(f"{current_text} is pure.")
    else:
        print(f"{current_text} is not pure!")

