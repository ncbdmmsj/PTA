x = list(map(int, input().split()))

while True:
    flag = int(input())
    if flag < 0 or flag > 24:
        break
    if x[flag] > 50:
        print(f"{x[flag]} Yes")
    else :
        print(f"{x[flag]} No")
