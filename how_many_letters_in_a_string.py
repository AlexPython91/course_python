# ✔ Пользователь вводит строку текста. +
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


user_string = input("Enter your string: ")

my_dict = {}

for elem in user_string:
    if elem in my_dict:
        my_dict[elem] += 1
    else:
        my_dict[elem] = 1

print(my_dict)

