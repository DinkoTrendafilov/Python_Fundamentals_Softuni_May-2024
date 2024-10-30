import random

number_to_guess = random.randint(1, 100)
guess = None
counter = 0

while True:
    guess = int(input("Познай числото между 1 и 100, имате 6 опита, успех!: "))

    if guess == number_to_guess:
        print(f"Браво!!! Ти позна числото, то бе: {number_to_guess}")
        break
    elif guess + 1 == number_to_guess or guess + 2 == number_to_guess \
            or guess - 1 == number_to_guess or guess - 2 == number_to_guess:
        print("Топло, топло!!!")
    elif guess < number_to_guess:
        print("Нагоре!")
    elif guess > number_to_guess:
        print("Надолу!")

    counter += 1
    if counter == 6:
        print("Нямате повече опити, съжаляваме :(, опитайте отново!")
        print(f"Търсеното число бе: {number_to_guess}")
        break
