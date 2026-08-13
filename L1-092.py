t = int(input())
while t > 0:
    t -= 1
    a, b, c = map(int, input().split())
    if a+b == c:
        print("Tu Dou")
    elif a*b == c:
        print("Lv Yan")
    else:
        print("zhe du shi sha ya!")