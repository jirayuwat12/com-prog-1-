n = int(input())
D = dict()
for _ in range(n):
    s = input().split()
    if s[0]+' '+s[1] in D:
        D[s[0]+' '+s[1]].append(s[2])
    else:
        D[s[0]+' '+s[1]] = [s[2]]
    if s[2] in D:
        D[s[2]].append(s[0]+' '+s[1] )
    else:
        D[s[2]] = [s[0]+' '+s[1]]
n = int(input())
for _ in range(n):
    s = input()
    if s in D:
        print(s,'-->',', '.join(sorted(D[s])))
    else:
        print(s,'-->','Not found')
# 6	
# Anthony Stark 02-111-1111	
# Henry Pym 02-222-2222	
# Anthony Stark 02-222-2222	
# Robert Banner 02-333-3333
# Robert Banner 02-444-4444
# Steven Rogers 02-222-2222	
# 6	
# 02-222-2222
# Anthony Stark
# Steven Rogers
# 911
# 02-444-4444
# 02-333-3333