n = int(input())

while n >0:
    n -= 1
    x, y = input().split()
    sa = 0
    sb = 0
    for i in x:
        sa += int(i)
    for i in y:
        sb += int(i)

    x = int(x)
    y = int(y)

    flag = False
    if x % sb == 0:
        if y % sa ==0:
            flag = True
        else:
            print("A")
    elif y % sa == 0:
        print("B")
    else:
        flag = True

    if flag:
        if x > y:
            print("A")
        else:
            print("B")
    # print(f"{x}  {y}  {sa}  {sb}  {chu_a}  {chu_b}")


