#вывести минмиальное значение из подсписков values
plain_list = []
#раскрываем подсписки  плоский список
for sublist in values:
    for num in sublist:
        plain_list.append(num)

if len(plain_list) == 0:
    print("Список пуст")
else:
    print(min(plain_list))
