#  Создайте функцию генератор чисел Фибоначчи

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Это для ввода, если без ввода, то просто строка n = input() не нужна
n = int(input('Please enter a number: '))
for i in range(n + 1):
    print(fibonacci(i))
