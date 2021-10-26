def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
 # คืนผลการทดสอบว่า a, b และ c เป็น coprime หรือไม่
 # อ่านนิยาม coprime ที่ https://en.wikipedia.org/wiki/Coprime_integers
    if gcd(a,b)==1 and gcd(a,c)==1 and gcd(b,c)==1:
        return True
    elif gcd(a,b)!=1:
        return gcd(gcd(a,b),c) == 1
    elif gcd(a,c)!=1:
        return gcd(gcd(a,c),b) == 1
    elif gcd(c,b)!=1:
        return gcd(gcd(c,b),a) == 1
    return False
    
def primitive_Pythagorean_triples(max_len):
    triple = []
    for x in range(1,max_len+1):
        for y in range(1,x+1):
            for z in range(1,y+1):
                if x**2 == y**2 + z**2 and is_coprime(x,y,z):
                    triple += [[x,z,y]]

    triple = sorted(triple) 
    ret = []
    for x in triple:
        ret += [[x[1],x[2],x[0]]]
    return ret
# exec(input().strip())
print(is_coprime(3,4,12), is_coprime(5,15,45),is_coprime(7,6,5),is_coprime(2,2,2))