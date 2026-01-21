n, k = map(int, input().split())
s_tasks = 0
i=1
res = 0

while i<=n:
    if s_tasks + i * 5 + k <= 240:
        s_tasks += i * 5
        res = i
        i=i+1
    else:
        break

print(res)
