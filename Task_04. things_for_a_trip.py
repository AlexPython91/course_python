# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант

WEIGHT_LIMIT = 15
things_dict = {
    'tent': 6,
    'sleeping bag': 4,
    'rug': 1,
    'thermal underwear': 7,
    'water filter': 1,
    'raincoat': 3
}

list_of_things = {}

sorted_gear = sorted(things_dict.items(), key=lambda x: x[1], reverse=True)
total_weight = 0

for item, weight in sorted_gear:
    if weight <= WEIGHT_LIMIT:
        list_of_things[item] = weight
        WEIGHT_LIMIT -= weight
        total_weight += weight

print("The following items fit in the backpack:")
for item, weight in list_of_things.items():
    print(f'{item} = {weight}')

print(f"Total weight = {total_weight}")
