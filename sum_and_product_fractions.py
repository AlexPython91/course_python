# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
MIXED = 1

try:
    first_fraction_numerator, first_fraction_denominator = map(int, input("Enter fraction 1 in the "
                                                                          "form a/b: ").split('/'))
    second_fraction_numerator, second_fraction_denominator = map(int, input("Enter fraction 2 in "
                                                                            "the form a/b: ").split('/'))
    first_fraction = Fraction(first_fraction_numerator, first_fraction_denominator)
    second_fraction = Fraction(second_fraction_numerator, second_fraction_denominator)

    if first_fraction_denominator == second_fraction_denominator:
        sum_fraction = Fraction(first_fraction_numerator + second_fraction_numerator, first_fraction_denominator)
        print(Fraction(sum_fraction))
        product_fractions = Fraction(first_fraction_numerator * second_fraction_numerator, second_fraction_denominator *
                                     second_fraction_denominator)
        print(Fraction(product_fractions))

    elif first_fraction_denominator != second_fraction_denominator:
        sum_fraction = Fraction(first_fraction_numerator * second_fraction_denominator + second_fraction_numerator *
                                first_fraction_denominator) / (first_fraction_denominator * second_fraction_denominator)
        print(Fraction(sum_fraction))
        product_fractions = Fraction(first_fraction_numerator * second_fraction_numerator, first_fraction_denominator *
                                     second_fraction_denominator)
        print(Fraction(product_fractions))

except ValueError:
    print('Incorrect fraction. Only fractional numbers')

