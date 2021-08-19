a = str(input())
b = str(input())
count = True
num = 0

def isalpha(x):
    return (x >= 'A' and x <= 'Z') or (x >= 'a' and x <= 'z')

for x in range(len(b)):
    
    if count and b[x] == a[0]:
        if x+len(a) == len(b):
            if b[x:x+len(a)] == a:
                num +=1
        else:
            if b[x:x+len(a)] == a and not isalpha(b[x+len(a)]):
                num +=1
    if isalpha(b[x]):
        count = False
    else:
        count = True
print(num)