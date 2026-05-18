N = int(input())
inp_list = []

# блок ввода значений - читаем построчно, режем по пробелам и обозначаем тип
# заполняем матрицу
for i in range(N):
    row = list(map(int, input().split()))
    inp_list.append(row)

# Вывод матрицы
for row in range(N-1, -1, -1):
    for col in range(N-1, -1, -1):
        print(inp_list[col][row], end=' ')
    print()
