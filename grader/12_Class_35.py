class roman :
    def __init__(self, r):
        self.r = r
        self.int = int(self)
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return self.r
    def __int__(self):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(self.r):
            if i+1<len(self.r) and self.r[i:i+2] in roman:
                num+=roman[self.r[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman[self.r[i]]
                i+=1
        return num
    def __add__(self, rhs):
        temp = int(self) + int(rhs)
        ret = ''
        num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        while temp:
            div = temp // num[i]
            temp %= num[i]
    
            while div:
                ret += sym[i]
                div -= 1
            i -= 1
        return roman(ret)

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
