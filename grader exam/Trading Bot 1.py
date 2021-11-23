n = int(input())
P = []
for x in range(n):
    i = input().split(',')
    P += [float(j) for j in i]
def ema7(index):
    a = 2/(1+7)
    return a * P[index] + EMA7[index-1]*(1-a)
def ema14(index):
    a = 2/(1+14)
    return a * P[index] + EMA14[index-1]*(1-a)

EMA7 = [0]*(n*7)
EMA14 = [0]*(n*7)
for i in range(n*7):
    if i == 6:
        EMA7[i] = (1/7) * sum(P[:7])
    if i == 13:
        EMA14[i] = (1/14) * sum(P[:14])
    if i > 6:
        EMA7[i] = ema7(i)
    if i > 13:
        EMA14[i] = ema14(i)
B = -1
S = -1
C = True
for i in range(13,n*7-1):
    if EMA7[i] <= EMA14[i] and EMA7[i+1] > EMA14[i+1] :
        B = i+1
        print("BUY at ",P[B])
        C = False
        B = -1
    elif EMA7[i] >= EMA14[i] and EMA7[i+1] < EMA14[i+1] :
        S = i+1
        print("SELL at ",P[S])
        C = False
        S =-1
if C:
    print("No results")
    
#80