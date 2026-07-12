n = int(input())
matrix = []
# 1. Исправлено: добавлена переменная цикла _ (или i)
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Внешний цикл по столбцам
for j in range(n):
    # Внутренний цикл по строкам
    for i in range(n):
        # 2. Исправлено: добавлен пробел при выводе, чтобы числа не слипались
        print(matrix[i][j], end=' ')
    print() # Перенос строки после каждого столбца

