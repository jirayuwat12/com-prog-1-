import math

bd,bm,by,d,m,y = [int(x) for x in input().split()]

numd = 0

leapyear = ((by-543) %400 == 0 or ((by-543)%4==0 and (by-543)%100 !=0))
ml = [31,28+leapyear,31,30,31,30,31,31,30,31,30,31]
numd = 0
for x in range(bm,12):
    numd += ml[x]  
numd += ml[bm-1]-bd+1

numd += 365*(y-by-1)

leapyear = ((y-543) %400 == 0 or ((y-543)%4==0 and (y-543)%100 !=0))
ml = [31,28+leapyear,31,30,31,30,31,31,30,31,30,31]
for x in range(m-1):
    numd += ml[x]
numd += d-1


p = round(math.sin((2*math.pi*numd)/(23)),2)
e = round(math.sin((2*math.pi*numd)/(28)),2)
i = round(math.sin((2*math.pi*numd)/(33)),2)

print(numd,format(p,".2f"),format(e,".2f"),format(i,".2f"))