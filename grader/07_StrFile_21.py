def rot13(x,i):
    x = chr(ord(x) + 13)
    if x == 'a':
        if(x>'z'):
            x = chr(ord('a') + ord(x) - ord('z')-1)
    print(x)
rot13('n','a')