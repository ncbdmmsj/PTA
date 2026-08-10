k = int(input())
M = list(map(int, input().split()))
Min = min(M)
Max = max(M)

a = list(mi * 10 for mi in M)
total = sum(a)

seat = [[0] * (Max * 10) for _ in range(k)]
x = 1
for i in range(Min * 10):
    if k == 1:
        seat[0][i] = x
        x += 2
    else:
        for j in range(k):
            seat[j][i] = x
            x += 1

index = [Min * 10 for _ in range(k)]
count = Min * 10 * k

pre = k - 1
x -= 1
while True:
    if total == count:
        break
    for i in range(k):
        if index[i] != a[i]:
            if pre == i:
                x += 2
            else:
                x += 1
            seat[i][index[i]] = x
            index[i] += 1
            count += 1
            pre = i

for i in range(k):
    print(f"#{i+1}", end="")
    for j in range(a[i]):
        if j % 10 == 0:
            print()
            print(f"{seat[i][j]}", end="")
        else:
            print(f" {seat[i][j]}", end="")
    print()