x = int(input())
while x:
    x -= 1
    sex, hight, weight = map(int,input().split())
    if sex == 0:
        if hight >129:
            print("ni li hai!",end="")
        elif hight <129:
            print("duo chi yu!",end="")
        else:
            print("wan mei!",end="")
        if weight >25:
            print("shao chi rou!")
        elif weight <25:
            print("duo chi rou!")
        else:
            print("wan mei!")
    else:
        if hight >129:
            print("ni li hai!",end="")
        elif hight <129:
            print("duo chi yu!",end="")
        else :
            print("wan mei!",end="")
        if weight >25:
            print("shao chi rou!")
        elif weight <25:
            print("duo chi rou!")
        else :
            print("wan mei!")
