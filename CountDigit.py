#какое число (30)
№Код вычисляет сумму цифр числа (\(7+3+4+0+8=22\)) и находит максимальную цифру (\(8\)), а затем складывает эти значения (\(22+8=30\)).

number = 73408
m = 0
s = 0
while number > 0:
    last_digit = number % 10
    s = s + last_digit
    if last_digit > m:
        m = last_digit
    number = number // 10
print(s + m)
