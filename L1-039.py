x = int(input())
s = input()

if len(s) % x:
    s += " "*(x - len(s) % x)
    # print(s)

for i in range(x):
    for j in range(len(s)-x+i, -1, -x):
        print(s[j], end="")
    print()