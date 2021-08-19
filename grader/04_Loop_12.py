n = int(input())
a = []
b = []
m = 1
minn = 0
maxx = 0
for i in range(n):
    t,tt = [int(x) for x in input().split(' ')]
    if m == 1:
        a += [t]
        b += [tt]
    else:
        a += [tt]
        b += [t]
    m *= -1
mode = str(input())
a.sort()
b.sort()
if mode == "Zig-Zag":
    print(a[0],b[-1])
else:
    print(b[0],a[-1])