i = input()
sum =0
num=0
while i!='q':
    i = float(i)
    sum+=i
    num+=1
    i = input()
if num == 0 :
    print("No Data")
else:
    print(format(sum/num,".2f"))