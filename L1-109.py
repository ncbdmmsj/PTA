s = input()
scores = list(map(int, input().split()))
cnt = [0]*26

num = 0
for i in s:
    cnt[ord(i)-97] += 1

for i in range(26):
    num += cnt[i]*scores[i]

for i in range(25):
    print(cnt[i], end=' ')
print(cnt[25])
print(num)
