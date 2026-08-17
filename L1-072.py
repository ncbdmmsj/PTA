a = []
for _ in range(3):
    row = list(map(int, input().split()))
    a.append(row)

x1 = 0
y1 = 0
num = 45
for i in range(3):
    for j in range(3):
        if a[i][j] == 0:
            x1 = i
            y1 = j
        num -= a[i][j]
a[x1][y1] = num

for _ in range(3):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    print(a[x][y])

b = [0, 0, 0, 0, 0, 0,
     10000, 36, 720, 360, 80, 252,
     108, 72, 54, 180, 72, 180,
     119, 36, 306, 1080, 144, 1800, 3600]

flag = int(input())

num = 0
if flag < 4:
    for i in range(3):
        num += a[flag-1][i]
elif flag < 7:
    for i in range(3):
        num += a[i][flag-4]
elif flag == 7:
    for i in range(3):
        num += a[i][i]
else:
    for i in range(3):
        num += a[i][2-i]

print(b[num])