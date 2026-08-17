n = int(input())
x = list(map(int, input().split()))

Min = 10e7
cnt1 = 0
Max = -1
cnt2 = 0

for i in range(n):
    if Min >= x[i]:
        if Min == x[i]:
            cnt1 += 1
        else :
            Min = x[i]
            cnt1 = 1

    if Max <= x[i]:
        if Max == x[i]:
            cnt2 += 1
        else:
            Max = x[i]
            cnt2 = 1
print(Min,cnt1)
print(Max,cnt2)
