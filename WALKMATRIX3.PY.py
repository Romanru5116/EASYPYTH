N, M = map(int, input().split())  # N строк и M столбцов
inp_list = []

# Блок ввода значений
for i in range(N):
    row = list(map(int, input().split()))
    inp_list.append(row)

# Вывод матрицы (обход столбцов слева направо)
for row in range(N - 1, -1, -1):
    for col in range(M):
        print(inp_list[row][col], end=' ')
    print()
