s = str(input())
ss = "0123456789"
for x in s:
    ss = ss.replace(x,'')
if ss == '':
    print("None")
else:
    print(ss[0],end='')
    for x in range(1,len(ss)):
        print(',',ss[x],sep='',end='')