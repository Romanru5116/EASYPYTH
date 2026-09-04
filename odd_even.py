#формируем_массив_нечетных чисел от n до n2_n = int(input())

# Если n четное, первое нечетное число будет n + 1, иначе n
start = n if n % 2 != 0 else n + 1

# Генерируем нечетные числа с шагом 2 и преобразуем в кортеж
result_tuple = tuple(range(start, n**2 + 1, 2))

print(result_tuple)
n = int(input())
