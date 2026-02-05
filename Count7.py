#сколько раз встречается цифра7
a=int(input())
c=0
while a>0:
 if a%10==7:
  c+=1
 a=a//10
print(c)
