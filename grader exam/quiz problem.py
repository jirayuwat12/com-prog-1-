n = int(input())
D = dict()
for _ in range(n):
    inp = input().split(' | ')
    if inp[0] == 'Play':
        rating = int(25 * (int(inp[2])+1)*(int(inp[3]) / 10**7))
        if not inp[1] in D:
            D[inp[1]] = {
                'rating' : rating,
                'level' : int(inp[2]),
                'score' : int(inp[3])
            }
        else:
            if rating > D[inp[1]]['rating']:
                D[inp[1]]['rating'] = rating
                D[inp[1]]['level'] = int(inp[2])
                D[inp[1]]['score'] = int(inp[3])
            elif rating == D[inp[1]]['rating']:
                if int(inp[2]) >D[inp[1]]['level']:
                    D[inp[1]]['rating'] = rating
                    D[inp[1]]['level'] = int(inp[2])
                    D[inp[1]]['score'] = int(inp[3])
                elif D[inp[1]]['level'] == int(inp[2]):
                    if int(inp[3]) >D[inp[1]]['score']:
                        D[inp[1]]['rating'] = rating
                        D[inp[1]]['level'] = int(inp[2])
                        D[inp[1]]['score'] = int(inp[3])
    if inp[0] == 'Rating' and len(inp) == 2:
        if inp[1] in D:
            print(D[inp[1]]['rating'])
        else:
            print(0)
    if inp[0] == 'Rating' and len(inp) == 1:
        L = []
        for x in D:
            L.append(D[x]['rating'])
        print(sum(L[:5]))
    if inp[0] == 'Detail':
        if inp[1] in D:
            print(inp[1],'|',D[inp[1]]['level'],'|',D[inp[1]]['score'],'|',D[inp[1]]['rating'])
        else:
            print(inp[1]+": No play history")

#70