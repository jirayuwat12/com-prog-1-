mode = str(input())
if mode == 'str2RLE':
    x = str(input())
    last = x[0]
    count = 1
    ans =""
    for i in x[1:]:
        if i == last:
            count+=1
        else:
            ans += last + ' '+str(count)+' '
            count = 1
            last = i
    ans += last + ' '+str(count) 
    print(ans)
elif mode == 'RLE2str':
    x = str(input())
    x = x.split(' ')
    for i in range(len(x)//2):
        print(x[2*i]*int(x[2*i+1]),end='')
else:
    print("Error")