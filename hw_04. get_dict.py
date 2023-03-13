# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def key_param_dict(**kwargs):
    return {v: k for k, v in kwargs.items()}


kwargs_list = [
    {'name': 'Алексей', 'age': 30, 'city': 'Самара'},
    {'name': 'Михаил', 'age': 25, 'city': 'Москва'},
    {'name': 'Екатерина', 'age': 40, 'city': 'Санкт-Петербург'}
]

for kwargs in kwargs_list:
    result = key_param_dict(**kwargs)
    print(result)
