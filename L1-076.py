k, price = map(int, input().split())
k = int(k)
price = float(price)

for i in range(k):
    x = float(input())
    if x < price:
        print(f"On Sale! {x}")