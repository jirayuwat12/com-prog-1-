x=  str(input())
a = ""
for i in x:
    if i == '(':
        a+='['
    elif i == '[':
        a+='('
    elif i == ')':
        a+=']'
    elif i == ']':
        a+=')'
    else:
        a += i
print(a)