#найти заданную подстроку
for i in messages:
    if substring.lower() in i.lower():
      print(i)
      break
else:
    print("Подстрока не найдена")





