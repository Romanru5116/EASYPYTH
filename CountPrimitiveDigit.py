#Алгоритм решения
Определить верхнюю границу: Поскольку нам нужны числа до 
 алгоритм решета должен работать в диапазонtе [2,n-1]
.
Инициализировать массив: Создать логический массив isPrime размером 2n
, заполнив его значениями true. Установить isPrime[0] = isPrime[1] = false.
Отсеять составные числа:
Проходить циклом Проходить циклом 
 от 2 до корень из 2х
 .
n=int(input())
limit = 2 * n + 1
n=int(input())
limit = 2 * n + 1
# Инициализируем массив для решета Эратосфена
sieve = [True] * limit
sieve[0] = sieve[1] = False
    
# Алгоритм Решета Эратосфена до 2n
for p in range(2, int(limit**0.5) + 1):
    if sieve[p]:
      for i in range(p * p, limit, p):
        sieve[i] = False
    
    # Считаем простые числа в интервале (n, 2n)
    count = sum(1 for p in range(n + 1, limit) if sieve[p])
print(count)


