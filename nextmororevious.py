#На вход программе поступает список из целых чисел. Ваша задача — вывести True, если элементы в списке отсортированы по неубыванию. В противном случае выведите False.
nums = list(map(int, input().split()))
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print("False")
        break
else:
    # Блок else сработает, только если цикл НЕ был прерван командой break
    print("True")
