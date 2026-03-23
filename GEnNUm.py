#генерация чисел нечетных от n до n^2
n=int(input())
# Генерация списка нечетных чисел в диапазоне [n, n2]
odd_numbers = [i for i in range(n, n**2 + 1) if i % 2 != 0]

# Вывод списка
print(odd_numbers)
