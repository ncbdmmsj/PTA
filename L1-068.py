n = int(input())
a = list(map(float, input().split()))

x = sum(1.0/x for x in a)
# fenmu = 1.0
# for i in a:
#     fenmu *= i
#
# fenzi = 0.0
# for i in a:
#     fenzi += fenmu/i

# fenmu *= n
print(f"{n/x:.2f}")