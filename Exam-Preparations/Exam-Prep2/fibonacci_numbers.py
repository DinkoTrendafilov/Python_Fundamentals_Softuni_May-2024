# Въвеждане на броя на числата от последователността на Фибоначи, които искаме да генерираме
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Начални стойности на последователността на Фибоначи
a, b = 0, 1

# Списък за съхраняване на числата от последователността на Фибоначи
fib_sequence = []

# Генериране на числата на Фибоначи
for i in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

# Принтиране на резултата
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
print(f"Sum of first {n} Fibonacci numbers are: {sum(fib_sequence)}")


