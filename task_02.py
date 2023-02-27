# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_NUM = 0
MAX_NUM = 100_000
count = 0

number = int(input(f"Enter number from {MIN_NUM} to {MAX_NUM}: "))

while number < MIN_NUM or number > MAX_NUM:
    print("That was no valid number.  Try again...")
    number = int(input(f"Enter number from {MIN_NUM} to {MAX_NUM}: "))
    try:
        if number == 0:
            raise ValueError
    except ValueError:
        print("0 is not in the range of available numbers to check")
        number = int(input(f"Enter number from {MIN_NUM} to {MAX_NUM}: "))

for i in range(2, number // 2 + 1):
    if number % i == 0:
        count += 1
if count <= 0:
    print("Is a prime number!")
else:
    print("Composite number!")
