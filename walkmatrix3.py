N, M = map(int, input().split())  # N строк и M столбцов
inp_list = []

# Блок ввода значений
for i in range(N):
    row = list(map(int, input().split()))
    inp_list.append(row)

# Вывод матрицы (обход столбцов справа налево)
for row in range(N):
    for col in range(M-1, -1, -1):
           print(inp_list[row][col], end=' ')
    print()