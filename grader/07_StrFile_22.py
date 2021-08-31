a = str(input())
b = str(input())
c = [0 for x in range(ord('Z')+1)] 
for x in a:
    c[ord(x.upper())] +=1
for x in b:
    c[ord(x.upper())] -=1
check = True
for x in range(ord('A'),ord('Z')+1):
    if c[x] != 0:
        check = False
# print(c)
if check:
    print("YES")
else:
    print("NO")