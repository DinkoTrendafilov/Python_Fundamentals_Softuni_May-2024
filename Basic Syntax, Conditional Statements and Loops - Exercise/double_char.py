while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue
    for ch in text:
        print(f"{ch}{ch}", end="")
    print()
