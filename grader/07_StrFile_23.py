filename,year = str(input()).split(' ')
j = open(filename)
lines = j.readlines()
year = year[-2:]
listpoint = []
sum = 0
for line in lines:
    y,point = str(line).split(' ')
    if point[-1] == '\n':
        point = point[:-1]
    if y[:2] == year:
        listpoint.append(float(point))
        sum += float(point)
if len(listpoint) != 0:
    print(min(listpoint),max(listpoint),sum / len(listpoint),sep= ' ')
else:
    print("No data")