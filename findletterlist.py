вводим символ и ищем в предложении, если есть выводим слово
s=input()
sentence=input()
words= sentence.split()
for i in words:
    if s in i.lower():
        print(i)
