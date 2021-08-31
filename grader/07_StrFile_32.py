password = str(input())
allch = True
error = [
    'Less than 8 characters',
    'No lowercase letters',
    'No uppercase letters',
    'No numbers',
    'No symbols',
    'Character repetition',
    'Number sequence',
    'Letter sequence',
    'Keyboard pattern'
]
#1
if len(password) < 8:
    print(error[0])
    allch = False
#2
lower = False
upper = False
sym = False
num = False
for x in password:
    if ord(x) >= ord('a') and ord(x) <= ord('z'):
        lower = True
    elif ord(x) >= ord('A') and ord(x) <= ord('Z'):
        upper = True
    elif ord(x) >= ord('0') and ord(x) <= ord('9'):
        num = True
    else:
        sym = True
if not lower:
    print(error[1])
    allch = False
if not upper:
    print(error[2])
    allch = False
if not num :
    print(error[3])
    allch = False
if not sym:
    print(error[4])
    allch = False
#3
last = password[0]
count =1
ch = False
for x in range(1,len(password)):
    if password[x] == last:
        count+=1
    else:
        last =password[x]
        count = 1
    if count>= 4:
        ch = True
        break
if ch:
    print(error[5])
    allch = False
#4
ch = False
for x in range(len(password)):
    if ord(password[x]) >= ord('0') and ord(password[x]) <= ord('9'):
        if ord(password[x-1]) >= ord('0') and ord(password[x-1]) <= ord('9'):
            direct = int(password[x]) - int(password[x-1])
            if direct == 0:
                continue
            count = 2
            for y in range(x-1,0,-1):
                if (ord(password[y-1]) >= ord('0') and ord(password[y-1]) <= ord('9') ):
                    if (int(password[y]) - int(password[y-1]) == direct)  or (password[y]=='9' and password[y-1]=='0'):
                        count +=1
                    else:
                        break
                else:
                    break
            if count >=4:
                ch = True
if ch:
    print(error[6])
    allch = False
#5
ch = False
password = password.upper()
for x in range(len(password)):
    if ord(password[x]) >= ord('A') and ord(password[x]) <= ord('Z'):
        if ord(password[x-1]) >= ord('A') and ord(password[x-1]) <= ord('Z'):
            direct = ord(password[x]) - ord(password[x-1])
            if direct == 0:
                continue
            count = 2
            for y in range(x-1,0,-1):
                if ord(password[y-1]) >= ord('A') and ord(password[y-1]) <= ord('Z'):
                    if ord(password[y]) - ord(password[y-1]) == direct:
                        count +=1
                    else:
                        break
                else:
                    break
            if count >=4:
                ch = True
if ch:
    print(error[7])
    allch = False
#6
patt= ['Q','W','E','R','T','Y','U','I','O','P']
patt2 = ['!','@','#','$','%','^','&','*','(',')','-','+']
patt3= ['Z','X','C','V','B','N','M']
patt4 = ['A','S','D','F','G','H','J','K','L']

def findpatt(c):
    for x in range(len(patt)):
        if patt[x] == c:
            return x
    return -1

ch = False
password = password.upper()
for x in range(1,len(password)):
    f = findpatt(password[x])
    fm = findpatt(password[x-1])
    if f != -1: 
        if fm != -1:
            direct = f - fm
            if not direct in [1,-1]:
                continue
            count = 2
            for y in range(x-1,0,-1):
                fxm = findpatt(password[y-1])
                fx = findpatt(password[y])
                if fxm != -1:
                    if fx - fxm == direct:
                        count +=1
                    else:
                        break
                else:
                    break
            if count >=4:
                ch = True

def findpatt2(c):
    for x in range(len(patt2)):
        if patt2[x] == c:
            return x
    return -1

password = password.upper()
for x in range(1,len(password)):
    f = findpatt2(password[x])
    fm = findpatt2(password[x-1])
    if f != -1: 
        if fm != -1:
            direct = f - fm
            if not direct in [1,-1]:
                continue
            count = 2
            for y in range(x-1,0,-1):
                fxm = findpatt2(password[y-1])
                fx = findpatt2(password[y])
                if fxm != -1:
                    if fx - fxm == direct:
                        count +=1
                    else:
                        break
                else:
                    break
            if count >=4:
                ch = True

def findpatt3(c):
    for x in range(len(patt3)):
        if patt3[x] == c:
            return x
    return -1

password = password.upper()
for x in range(1,len(password)):
    f = findpatt3(password[x])
    fm = findpatt3(password[x-1])
    if f != -1: 
        if fm != -1:
            direct = f - fm
            if not direct in [1,-1]:
                continue
            count = 2
            for y in range(x-1,0,-1):
                fxm = findpatt3(password[y-1])
                fx = findpatt3(password[y])
                if fxm != -1:
                    if fx - fxm == direct:
                        count +=1
                    else:
                        break
                else:
                    break
            if count >=4:
                ch = True
def findpatt4(c):
    for x in range(len(patt4)):
        if patt4[x] == c:
            return x
    return -1

password = password.upper()
for x in range(1,len(password)):
    f = findpatt4(password[x])
    fm = findpatt4(password[x-1])
    if f != -1: 
        if fm != -1:
            direct = f - fm
            if not direct in [1,-1]:
                continue
            count = 2
            for y in range(x-1,0,-1):
                fxm = findpatt4(password[y-1])
                fx = findpatt4(password[y])
                if fxm != -1:
                    if fx - fxm == direct:
                        count +=1
                    else:
                        break
                else:
                    break
            if count >=4:
                ch = True


if ch:
    print(error[8])
    allch = False
if allch:
    print('OK')