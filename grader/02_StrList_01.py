n = str(input())
n += str((11 - ( sum([(13-x)*int(n[x]) for x in range(12)])%11))%10)
print(n[0],n[1:5],n[5:10],n[10:12],n[12],sep= ' ' )