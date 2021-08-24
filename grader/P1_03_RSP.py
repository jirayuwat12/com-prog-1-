l = 0
r = 0
al = 0
m = int(input())
while max(l,r) < m and al != 3*m:
    L,R = [x for x in input().split(' ')]
    if L == 'R' and R == 'S':
        l+=1
    elif L == 'S' and R == 'R':
        r+=1
    elif L == 'S' and R == 'P':
        l+=1
    elif L == 'P' and R == 'S':
        r+=1
    elif L == 'P' and R == 'R':
        l+=1
    elif L == 'R' and R == 'P':
        r+=1
    al+=1
if max(l,r) != m:
    print(l,' ',r,'\n','Tie',sep='')
elif l < r:
    print(l,' ',r,'\n','Player 2 wins',sep='')
else:
    print(l,' ',r,'\n','Player 1 wins',sep='')
