#Формат ввода
#На первой строке вводится натуральное число N — количество пунктов рецепта.
#Далее следуют N строк — пункты рецепта.
n = int(input())
res = []

for i in range(n):
    s = input()
    if "соль" not in s:
        res.append(s)

print(", ".join(res))
