# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух
# других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
# существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("This is an equilateral triangle")
    elif a == b or b == c or c == a:
        print("This is an isosceles triangle")
    else:
        print("This is a scalene triangle")
else:
    print("These sides do not form a triangle")


