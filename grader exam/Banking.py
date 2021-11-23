db = dict()
n = int(input())
for _ in range(n):
    n,a,m = input().split()
    db[a] = {
        'name' : n,
        'amount' : float(m)
    }
inp = input()
L = []
def deposit(name,acc,amount):
    if acc in db:
        if name == db[acc]['name']:
            db[acc]['amount'] += amount
            L.append(db[acc]['name']+' '+'(' +acc+ ')'+' '+str(db[acc]['amount']))
        else:
            L.append('Transaction Failed')
    else:
        db[acc] = {
            'name' : name,
            'amount' : amount
        }
        L.append(db[acc]['name']+' '+'(' +acc+ ')'+' '+str(db[acc]['amount']))

def withdraw(name, acc,amount):
    if acc in db:
        if name == db[acc]['name']:
            if amount < db[acc]['amount']:
                db[acc]['amount'] -= amount
                L.append(db[acc]['name']+' '+'(' +acc+ ')'+' '+str(db[acc]['amount']))
            else:
                L.append('Transaction Failed')
        else:
            L.append('Transaction Failed')
    else:
        L.append('Transaction Failed')
def transfer(name, acc,amount,to):
    if acc in db:
        if name == db[acc]['name']:
            if amount < db[acc]['amount']:
                db[acc]['amount'] -= amount
            else:
                L.append('Transaction Failed')
                return
        else:
            L.append('Transaction Failed')
            return
    else:
        L.append('Transaction Failed')
        return
    if to in db:
        db[to]['amount'] += amount
        L.append(db[acc]['name']+' '+'(' +acc+ ')'+' '+str(db[acc]['amount']))
        L.append(db[to]['name']+' '+'(' +to+ ')'+' '+str(db[to]['amount']))

    else:
        db[acc]['amount'] += amount
        L.append('Transaction Failed')

while inp != 'exit':
    inp = inp.split()
    if inp[2] == 'deposit':
        deposit(name = inp[0] ,acc = inp[1],amount = float(inp[3]))
    if inp[2] == 'withdraw':
        withdraw(name = inp[0], acc = inp[1],amount= float(inp[3]))
    if inp[2] == 'transfer':
        transfer(name = inp[0], acc = inp[1],amount = float(inp[4]),to = inp[3])
    inp = input()
for i in L:
    print(i)

#12