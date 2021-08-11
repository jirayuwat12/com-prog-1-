inp = input("")
if inp[-1] == 's' or inp[-1] == 'x' or inp[-2:] == 'ch':
    print(inp + 'es')
elif inp[-1] == 'y' and inp[-2] not in ['a','e','i','o','u']:
    print(inp[:-1] + 'ies')
else :
    print(inp+'s')