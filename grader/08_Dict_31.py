p={100:3, 10:5, 5:10, 1:7}
def total(pocket):
    sum = 0
    for x in pocket:
        sum += x *pocket[x]
    return sum

def take(pocket, money_in):
    for x in money_in:
        if x in pocket:
            pocket[x] += money_in[x]
        else:
            pocket[x] = money_in[x]
    return pocket

def pay(pocket, amt):
    bank = sorted(pocket)
    ind = len(bank)-1
    ret ={}
    while amt > 0 and ind>=0:
        if amt // bank[ind] == 0:
            ind -=1
            continue
        if bank[ind] in ret:
            total = pocket[bank[ind]]

            ret[bank[ind]] += min(amt // bank[ind],total)
        else:
            total = pocket[bank[ind]]
            ret[bank[ind]] = min(amt // bank[ind],total)
        amt = amt - bank[ind]*ret[bank[ind]]
        ind -=1
    # print(amt)
    if amt > 0:
        return {}
    else:
        for x in ret:
            pocket[x] -= ret[x]
        return ret
print(pay(p, 68))
print(p)
# exec(input().strip()) 