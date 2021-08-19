x = str(input())
last = x[0]
count = 1
a = ""
for i in x[1:]:
    if i==last:
        count+=1
    else:
        a += last + ' ' + str(count)+' '
        last = i
        count = 1
a += last + ' ' + str(count)+' '
print(a)