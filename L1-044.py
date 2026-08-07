x = input()
x = int(x)
s = input()
float = 0
while s != "End":
    if float == x:
        print(s)
        float = 0
        s = input()
        continue
    float = float + 1

    if s == "Bu":
        print("JianDao")
    elif s == "JianDao":
        print("ChuiZi")
    else :
        print("Bu")
    s = input()
