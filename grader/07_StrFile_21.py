def rot13(ch):
    if ch >='a' and ch <= 'z':
        i = ord(ch) + 13
        if i > ord('z'):
            i = ord('a') + i - ord('z') -1
        return chr(i)
    elif ch >='A' and ch <='Z':
        i = ord(ch) +13
        if i>ord('Z'):
            i = ord('A') + i - ord('Z') -1
        return chr(i)
    else:
        return ch

i = str(input())
while i != 'end':
    a =""
    for x in i:
        a+=rot13(x)
    print(a)
    i = str(input())

