a = float(input('Введите длину отрезка А '))
b = float(input('Введите длину отрезка B '))
c = float(input('Введите длину отрезка C '))

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
elif a == b + c or b == a + c or c == a + b:
    print('Это вырожденный треугольник')
else:
    print('Такого треугольника не существует')
