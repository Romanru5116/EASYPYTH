#Разбить этот список на k вложенных списков, каждый из которых должен состоять из r элементов. Гарантируется, что будет выполняться условие:
#k
#×
#r
#=
#k×r=n
n=int(input())
list_in = list(map(int, input().split()))
k, r = map(int, input().split())
list_out=[]

idx = 0  # Индекс для прохода по исходному списку
for i in range(k):
    row = []
    for j in range(r):
        #проходим по строчкам
        if idx < n:
            row.append(list_in[idx])
            idx += 1
    list_out.append(row)

print(list_out)