# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

ZERO_CHECK: int = 0
HEX_REMAINDER: int = 16

hex_map: dict = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
}

number: int = int(input("Enter a number: "))

if number == ZERO_CHECK:
    hex_str = '0'
else:
    hex_str = ''
    while number > 0:
        remainder = number % HEX_REMAINDER
        hex_str = hex_map[remainder] + hex_str
        number //= 16

print("Hexadecimal string representation:", hex_str)
