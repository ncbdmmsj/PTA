a, b = map(int, input().split())
x = list(map(int,input().split()))

cntb = x.count(1)
cnta = x.count(0)

if cntb==3:
    print(f"The winner is b: {b} + 3")
elif cnta==3:
    print(f"The winner is a: {a} + 3")
elif a > b:
    if cnta > 0:
        print(f"The winner is a: {a} + {cnta}")
    else :
        print(f"The winner is b: {b} + {cntb}")
else :
    if cntb > 0:
        print(f"The winner is b: {b} + {cntb}")
    else :
        print(f"The winner is a: {a} + {cnta}")