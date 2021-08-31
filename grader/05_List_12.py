l1 = ['Robert',
'William',
'James' ,
'John' ,
'Margaret',
'Edward',
'Sarah' ,
'Andrew',
'Anthony',
'Deborah'
]
l2 = [
'Dick',
'Bill',
'Jim',
'Jack',
 'Peggy',
'Ed',
'Sally',
'Andy',
'Tony',
'Debbie',
]
n = int(input())
for _ in range(n):
    name = str(input())
    l1index = -1
    l2index = -1
    for _ in range(10):
        if l1[_] == name:
            l1index=_
        elif l2[_] == name:
            l2index=_
    if l1index != -1:
        print(l2[l1index])
    elif l2index != -1:
        print(l1[l2index])
    else:
        print("Not found") 