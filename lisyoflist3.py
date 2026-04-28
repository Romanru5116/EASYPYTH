# values содержит несколько списков
# 1. Подсчет общего количества элементов
total_elements = sum(len(sublist) for sublist in values)
print(total_elements)

# 2. Подсчет подсписков, содержащих хотя бы один элемент (не пустых)
non_empty_sublists = sum(1 for sublist in values if len(sublist) > 0)
print(non_empty_sublists)
#логика
#Общее количество элементов: Мы проходим циклом по каждому sublist (подсписку) внутри values, берем его длину #len(sublist) и суммируем эти длины с помощью функции sum().
#Количество непустых подсписков: Мы проходим по подспискам и используем условие if len(sublist) > 0 (или просто if #sublist), чтобы посчитать только те, в которых есть элементы.




