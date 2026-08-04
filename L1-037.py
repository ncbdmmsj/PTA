x,y = input().split()
x = int(x)
y = int(y)
if y == 0:
    print(f"{x}/0=Error")
elif y<0:
    print(f"{x}/({y})={x/y:.2f}")
else :
    print(f"{x}/{y}={x/y:.2f}")