@ расчет суммф цифр в числе
n= int(input()) 
s=0
while n: 
  s += n % 10
  n= n//10 
print(s)
