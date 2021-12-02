f = open('data.txt')

def commas(x):
    x = x[::-1]
    ret = ''
    for i in range(len(x)):
        if i %3 ==0 and i != 0:
            ret += ','
        ret += x[i]
    return ret[::-1]
for line in f:
    s = ''
    temp = ''
    stt = False
    mstt  = False
    for i in line[:-1]:
        if ord(i)==ord('0') and not stt:
            mstt = True
        if i == ' ':
            mstt = False
        if 1 <= ord(i) - ord('0') <= 9 and not stt and not mstt:
            stt = True
        elif not (0 <= ord(i) - ord('0') <= 9) and stt and not mstt:
            stt = False
            s += commas(temp)
            temp = ''
        if not stt:
            s += i
        if stt:
            temp += i
    if temp != '':
        s += commas(temp)
    print(s)
f.close()
