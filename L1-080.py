x, y, n = map(int, input().split())
flag = 2
a = [x, y]

pos1 = 0
pos2 = 1
while flag <= n:
    z = a[pos1] * a[pos2]
    pos1 += 1
    pos2 += 1
    if z//10 == 0:
        a.append(z)
        flag += 1
    else:
        a.append(z//10)
        a.append(z%10)
        flag += 2
for i in range(n-1):
    print(a[i], end=" ")
print(a[n-1])