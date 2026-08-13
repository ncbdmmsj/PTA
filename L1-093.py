n = int(input())
x = list(map(int, input().split()))

t = int(input())
while t > 0:
    t -= 1
    test = list(map(int, input().split()))
    flag = True
    cnt = 0
    for i in range(len(test)):
        if test[i] != 0 and test[i] != x[i]:
            flag = False
        if test[i] == 0:
            cnt += 1
    if flag and cnt != n:
        print("Da Jiang!!!")
    else :
        print("Ai Ya")