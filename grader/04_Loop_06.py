n = int(input())

print(' '*(n-1),'*',' '*((1-1)*2-1),sep='')
for x in range(2,n):
    print(' '*(n-x),'*',' '*((x-1)*2-1),'*',sep='')
print('*'*(n*2-1))