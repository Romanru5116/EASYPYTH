# определем являетс ли матрица симметричной
n = int(input())
matrix = []

for _ in range(n):
    # Считываем строку, разбиваем её по пробелам и превращаем каждое значение в int
    row = list(map(int, input().split()))
    
    # Если введенных элементов меньше n, заполняем оставшиеся нулями
    if len(row) < n:
        row.extend([0] * (n - len(row)))
        
    matrix.append(row) # Добавляем строку в матрицу

is_symmetric = True

for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break  # Выходим из внутреннего цикла при первой несимметричности
    if not is_symmetric:
        break      # Выходим из внешнего цикла

if is_symmetric:
    print("Yes")
else:
    print("No")
     



