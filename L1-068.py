n = int(input())
a = list(map(float, input().split()))

fenmu = 1.0
for i in a:
    fenmu *= i

fenzi = 0.0
for i in a:
    fenzi += fenmu/i

fenmu *= n
print(f"{fenmu/fenzi: .2f}")