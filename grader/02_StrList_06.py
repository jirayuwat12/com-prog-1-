inp1 = input()
inp2 = input()
inp1 = inp1.replace('[','')
inp1 = inp1.replace(']','')
inp1 = inp1.replace(',','')
inp2 = inp2.replace('[','')
inp2 = inp2.replace(']','')
inp2 = inp2.replace(',','')
list1 = inp1.split(' ')
list1 = [float(x) for x in list1]
list2 = inp2.split(' ')
list2 = [float(x) for x in list2]
list3 = []
for x in range(len(list1)):
    list3.append(list1[x] + list2[x])
print(list1,'+',list2,'=',list3,sep=' ')