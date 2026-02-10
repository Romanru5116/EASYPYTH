# найти сумму делителей
n= int(input())
s = 0
i=1

while i<=n:
    if n % i == 0:
        s += i
    i=i+1 
print(s)
