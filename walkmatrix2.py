N = int(input())
inp_list = []

# блок ввода занчений

for i in range(N):
    row = list(map(int, input().split()))
    inp_list.append(row)

# Вывод матрицы (поворот на 90 градусов против часовой стрелки или транспонирование с разворотом)
for row in range(N-1, -1, -1):
    for col in range(N-1, -1, -1):
        print(inp_list[col][row], end=' ')
    print()
