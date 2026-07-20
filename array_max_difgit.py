# на вход подаем 2 числа - размерность массива и дале построчно значения массива
# найти максимальное значение элементов в массиве
# Считываем размеры массива n и m
n, m = map(int, input().split())
# Считываем элементы массива (построчно)
array = [list(map(int, input().split())) for _ in range(n)]
max_val= None
max_ind_n=0
max_ind_m=0
for i in range(n):
    for j in range(m):
        val = array[i][j] # Получаем значение текущего элемента
        # Если нашли элемент больше или это первый элемент вообще
        if max_val is None or val > max_val:
            max_val = val
            max_ind_n, max_ind_m = i, j
print (max_val)
print(max_ind_n, max_ind_m)
