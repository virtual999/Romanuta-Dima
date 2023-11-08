g = int(input())
b = int(input())
c = int(input())
if g == b == c:
    print('Треугольник равносторонний')
if g == b != c or b == c != g or c == g != b:
    print('Треугольник равнобедренный')
if g != b !=c:
    print('Треугольник разносторонний')