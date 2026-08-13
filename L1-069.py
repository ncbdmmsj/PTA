x = list(map(int, input().split()))
m = max(x[:4])

cntya = 0
cntyu = 0
flag = 0

for i in range(4):
    if x[i] < x[4]:
        cntya += 1
        flag = i+1
    if m - x[i] >x[5]:
        cntyu += 1
        flag = i+1

if cntya == 0 and cntyu == 0 :
    print("Normal")
elif cntyu + cntya > 1 :
    print("Warning: please check all the tires!")
else :
    print(f"Warning: please check #{flag}!")
