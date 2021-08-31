f1,f2 = [x for x in input().split()]
data1 = open(f1)
data2 = open(f2)
lines1 = data1.readlines()
lines2 = data2.readlines()
lines1 = lines1+lines2
L = []
D = {}
for line in lines1:
    ID, Grade = [x for x in line.split()]
    D[ID[-2:] + ID[:-2]] = Grade

for x in sorted(D.keys()):
    print(x[2:]+x[:2],D[x],sep=' ')
