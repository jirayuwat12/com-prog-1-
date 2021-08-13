text = str(input())
i = 3
x = ""
y = ""
while i < len(text):
    x += text[i]
    i+=7
i = 7
while i < len(text):
    y += text[i]
    i+=5
# print(x,y)
ans = int(x) + int(y) + 10000
ans = str(ans)
ans = ans[-4:-1]
sum = 0
for i in ans:
    sum += int(i)
print(ans,chr(ord('A') -1 +int(str(sum)[-1])+1),sep='')
