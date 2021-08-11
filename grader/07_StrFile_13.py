inp= input("")
ans = ""
isCap = False
firstInclude = False
for i in inp:
    if (i >= 'a' and i <= 'z') or (i >='A' and i<='Z') or (i>='0' and i<='9'):
        if isCap:
            ans += i.upper()
            isCap = False
        else :
            ans += i.lower()
        firstInclude = True
    elif firstInclude:
        isCap = True
        continue
print(ans)