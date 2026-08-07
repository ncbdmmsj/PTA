k = input()
k = int(k)
while k :
    name, x, y = input().split()
    x = int(x)
    y = int(y)
    k = k - 1
    if (x < 15  or x > 20) or (y < 50 or y > 70):
        print(name)

