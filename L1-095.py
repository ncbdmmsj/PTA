import math
n0, n1, n = map(int, input().split())

nq = (n0 + n1) / n
# print(q)

home_n0 = math.floor(n0 / nq)
if home_n0 == 0:
    home_n0 = 1

flag0 = False
x = n if n < n0 else n0
for i in range(home_n0, x):
    if n0%i == 0 and n1%(n-i) == 0:
        home_n0 = i
        flag0 = True
        break

home_n1 = math.floor(n1 / nq)
if home_n1 == 0:
    home_n1 = 1

flag1 = False
x = n if n < n1 else n1
for i in range(home_n1, x):
    if n1 % i == 0 and n0 % (n-i) == 0:
        home_n1 = i
        flag1 = True
        break

if flag0 and flag1:
    cha = abs(n0/home_n0 - n1/(n-home_n0))-abs(n1/home_n1 - n0/(n-home_n1))
    if home_n0 != n0 and n - home_n0 != n1:
        if home_n1 != n1 and n - home_n1 != n0:
            if cha < 0:
                print(home_n0, n-home_n0)
            else :
                print(n-home_n1, home_n1)
        else :
            print(home_n0, n-home_n0)
    else :
        if home_n1 != n1 and n - home_n1 != n0:
            print(n-home_n1, home_n1)
        else :
            print("No Solution")
elif flag0 and home_n0 != n0 and n - home_n0 != n1:
    print(home_n0, n-home_n0)
elif flag1 and home_n1 != n1 and n - home_n1 != n0:
    print(n-home_n1, home_n1)
else:
    print("No Solution")