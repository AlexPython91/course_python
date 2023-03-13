# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с
# именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на
# процент премии


def calculate_premium(names, rates, premiums) -> dict:
    calculation = {name: rate * float(premium.strip('%')) / 100 for name, rate, premium
                   in zip(names, rates, premiums)}
    return calculation


names = ['Alex', 'Ivan', 'Gregory']
rates = [14, 15, 22]
premiums = ['10.25%', '15%', '12.5%']
result_dict = calculate_premium(names, rates, premiums)
print(result_dict)
