# Дан список повторяющихся элементов. +
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

my_list = [1, 'Hello', 3.14, True, None, 2.36, 28, 'World', 28, 1, 'Hello']

new_list = []

for elem in my_list:
    if elem not in new_list and my_list.count(elem) > 1:
        new_list.append(elem)
print(f'{my_list = }\n{new_list = }')
