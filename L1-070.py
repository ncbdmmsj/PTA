cnt = 0
fristflag = 0
cntflag = 0

while True:
    s = input()
    if s == ".":
        break
    cnt += 1
    if s.find("chi1 huo3 guo1") != -1:
        cntflag += 1
        if fristflag == 0:
            fristflag = cnt

print(f"{cnt}")
if cntflag > 0:
    print(f"{fristflag} {cntflag}")
else :
    print("-_-#")