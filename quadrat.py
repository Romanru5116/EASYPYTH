grid = [input().strip() for _ in range(4)]

found = False
for i in range(3):
    for j in range(3):
        # Проверяем квадрат 2x2 с левым верхним углом (i, j)
        c = grid[i][j]
        if grid[i][j + 1] == c and grid[i + 1][j] == c and grid[i + 1][j + 1] == c:
            print("No")
            found = True
            break
    if found:
        break

if not found:
    print("Yes")

        



