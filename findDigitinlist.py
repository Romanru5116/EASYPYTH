nums = list(map(int, input().split()))
r = int(input())
# Используем len(nums), чтобы проверить все элементы, включая последний
for i in range(len(nums)):
    if nums[i] == r:
        print(i + 1)  # Вывод позиции (начиная с 1)
        break
else:
    print("ErrorValue")
