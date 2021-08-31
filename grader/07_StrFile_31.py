dna = str(input())
dna = dna.upper()
mod = str(input())
for x in dna:
    if not x in ['A','T','C','G']:
        print("Invalid DNA")
        break
else: 
    if mod == 'R':
        ans = ""
        for x in dna:
            if x == 'A':
                ans += 'T'
            elif x=='T':
                ans+='A'
            elif x=='C':
                ans+='G'
            else:
                ans+='C'
        ans = ans[::-1]
        print(ans)
    if mod == 'F':
        dic = {
            "A":0,
            "T":0,
            "G":0,
            "C":0
        }
        for x in dna:
            dic[x] +=1
        print('A','=',dic['A'],', ',sep ='',end='')
        print('T','=',dic['T'],', ',sep ='',end='')
        print('G','=',dic['G'],', ',sep ='',end='')
        print('C','=',dic['C'],sep ='',end='')
    if mod =='D':
        sum = 0
        pat = str(input())
        for x in range(len(dna)):
            if dna[x:x+2] == pat:
                sum +=1
        print(sum)