i,j = [int(k) for k in input().split()]
T = []
for x in range(i):
    T.append([x for x in input()])
target = str(input())
ans = ['.']*len(target)
def search(y,x,index=0,ret = []):
    if y < 0 or y >= i or x < 0 or x >= j:
        return
    if index == len(target) and len(ret) != 0:
        # print(ret)
        for x in range(len(ret)):
            ans[x] = ret[x]
        return
    # print(x,y,index)
    if T[y][x] == target[index]:
        search(y+1,x,index+1,ret+[(y,x)])
        search(y-1,x,index+1,ret+[(y,x)])
        search(y,x-1,index+1,ret+[(y,x)])
        search(y,x+1,index+1,ret+[(y,x)])

for y in range(i):
    for x in range(j):
        search(y,x)  
print(ans)

#100