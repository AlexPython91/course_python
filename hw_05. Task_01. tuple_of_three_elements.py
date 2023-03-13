# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж
# из трёх элементов: путь, имя файла, расширение файла.

def parse_path(filepath):

    components = filepath.split('/')
    filename = components[-1]
    path = '/'.join(components[:-1])

    name_parts = filename.split('.')
    name = '.'.join(name_parts[:-1])
    extension = '.' + name_parts[-1]

    return (path, name, extension)


path, name, extension = parse_path('/User/Users/Alex91/Documents/report.txt')
print(f'Path: {path}')
print(f'Filename: {name}')
print(f'Extension: {extension}')
