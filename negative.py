# сравниваем 2 картинки - исходную  и обработанную (негатив)
n, m = map(int, input().split())

original = [input() for _ in range(n)]
input()
mishutka = [input() for _ in range(n)]

errors = 0
for i in range(n):
    for j in range(m):
        orig_pixel = original[i][j]
        mish_pixel = mishutka[i][j]
        
        expected = 'W' if orig_pixel == 'B' else 'B'
        
        if mish_pixel != expected:
            errors += 1

print(errors)



