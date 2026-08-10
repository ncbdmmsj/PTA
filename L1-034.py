n = int(input())

p = [0] * 1001
count = 0
zhi = 0
while n:
    x = list(map(int, input().split()))

    for i in x[1:]:
        p[i] = p[i] + 1
        if p[i] > count or (p[i] == count and i > zhi):
            zhi = i
            count = p[i]

    n -= 1

print(f"{zhi} {count}")