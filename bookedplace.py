# Вы работаете над системой управления бронированием мест в кинотеатре.
Пример входных данных (переменная booked уже определена)
# booked = ["Р.1, М.5", "Р.2, М.2", "Р.5, М.10"]

rows = 5
seats_per_row = 10

for r in range(1, rows + 1):
    row_display = []
    for m in range(1, seats_per_row + 1):
        # Формируем строку для проверки в списке booked
        seat_str = f"Р.{r}, М.{m}"
        
        if seat_str in booked:
            row_display.append("X")
        else:
            row_display.append("O")
    
    # Выводим ряд, объединяя элементы через пробел
    print(" ".join(row_display))
