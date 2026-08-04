x = input()
x = int(x)
for i in range(x):
    c,y = input().split()
    y = float(y)
    if c =="F":
        y = y*1.09
    else :
        y = y/1.09
    print(f"{y:.2f}")