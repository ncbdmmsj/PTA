s = input()
if len(s) > 4:
    new_s = s[:4] + "-" + s[4:]
elif s[1] > '1' and s[0] >= '2':
    new_s = "19" + s[:2] + "-" + s[2:]
else :
    new_s = "20" + s[:2] + "-" + s[2:]
print(new_s)
