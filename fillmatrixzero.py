n = int(input('Введите размер квадратной матрицы: '))

a = []
for i in range(n):
    a.append([0] * n)

# Выводим пустую матрицу
for row in a:
    print(row)
