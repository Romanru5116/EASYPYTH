#При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита:
n=int(input())
from string import ascii_uppercase
b = list(ascii_uppercase[:n])
print(b)
