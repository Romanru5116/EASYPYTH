#решаемая задача: посчитать сумму по строкм  и столбцам для заданной матрицы
N, M = map(int, input().split())
matrix = []

for _ in range(N):
    # Считываем строку, разбиваем её по пробелам и превращаем каждое значение в int
    row = list(map(int, input().split()))
    matrix.append(row)

# Перебираем все строки матрицы
for i in range(N):
    row_sum = 0  # Сбрасываем сумму для каждой новой строки
    for j in range(M):
        row_sum += matrix[i][j]  # копим сумму строки
    print(row_sum,end=' ')  # Выводим сумму строки (сдвиг отступа важен)
print() #перевод строки
for j in range(M):
    col_sum = 0  # Сбрасываем сумму для каждого столбца
    for i in range(N):
        col_sum += matrix[i][j]  # копим  сумму столбца
    print(col_sum,end=' ')  # Выводим сумму 
