N, M = list(map(int, input().split()))
arr = []
for i in range(0, N):
    arr.append(list(map(int, input())))


def iceCream(x, y):
    if x < 0 or x>=N or y <0 or y>=M:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        iceCream(x - 1, y)
        iceCream(x + 1, y)
        iceCream(x, y - 1)
        iceCream(x, y + 1)
        return True
    else:
        return False




count = 0
for i in range(0, N):
    for j in range(0, M):
        if iceCream(i, j) ==True:
            count += 1

print(count)
