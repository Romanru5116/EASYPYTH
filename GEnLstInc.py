№генератор списка с условием четности
n = int(input())
result = [i**2 for i in range(n + 1) if i % 2 == 0]
print(result)                  
