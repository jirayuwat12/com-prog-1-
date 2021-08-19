a = str(input())
b = str(input())

if len(a) != len(b):
    print("Incomplete answer")
else:
    num = 0
    for x in range(len(a)):
        if a[x] == b[x]:
            num+=1
    print(num)