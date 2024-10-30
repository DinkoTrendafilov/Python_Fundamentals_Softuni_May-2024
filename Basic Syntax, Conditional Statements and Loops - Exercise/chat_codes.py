number_of_loop = int(input())

for i in range(1, number_of_loop + 1):
    current_number = int(input())
    if current_number == 88:
        print("Hello")
    elif current_number == 86:
        print("How are you?")
    elif current_number < 88:
        print("GREAT!")
    elif current_number > 88:
        print("Bye.")
