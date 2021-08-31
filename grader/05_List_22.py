i = input()
dict= {}
while i != 'q':
    ID,grade =[str(x) for x in i.split()]
    dict[ID] = grade.upper()
    i = input()
i = [str(x) for x in input().split()]
for x in i:
    if dict[x][0]=='F':
        dict[x] = 'D'
    elif dict[x] == 'A':
        continue
    elif len(dict[x]) == 2:
        dict[x] = chr(ord(dict[x][0]) -1)
    else:
        dict[x] += '+'
for x in sorted(dict.keys()):
    print(x,dict[x],sep=' ')