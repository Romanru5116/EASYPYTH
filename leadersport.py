n,m=map(int,input().split())
# Инициализируем переменные для хранения данных лучшего спортсмена
best_athlete = -1
max_best_throw = -1
max_total_sum = -1

# Поочередно обрабатываем результаты каждого спортсмена
for i in range(n):
    # Считываем броски текущего спортсмена
    throws = list(map(int, input().split()))
    
    # Находим лучший бросок и сумму всех попыток
    current_best = max(throws)
    current_sum = sum(throws)
    
    # Проверяем, побеждает ли текущий спортсмен по правилам:
    # 1. Его лучший бросок строго больше, чем у предыдущего лидера
    # 2. Или лучший бросок равен лидеру, но сумма результатов строго больше
    if (current_best > max_best_throw) or \
       (current_best == max_best_throw and current_sum > max_total_sum):
        
        max_best_throw = current_best
        max_total_sum = current_sum
        best_athlete = i
        # Третье условие (минимальный номер при равенстве) выполняется автоматически,
        # так как мы используем строгое сравнение (>), и первый найденный при равенстве останется лидером.

# Выводим номер победителя
print(best_athlete)


