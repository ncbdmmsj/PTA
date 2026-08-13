l, k = map(int, input().split())
while k > 0:
    k -= 1
    s = input()
    x = 0
    flag = 0
    for i in s:
        if i == 'n':
            if flag == 0:
                flag = 1
            else:
                x *= 2
            x += 1
        else :
            x *= 2
    x += 1
    print(x)