def reverse(d):
    ret = {}
    for x in d:
        ret[d[x]] = x
    return ret
def keys(d, v):
    ret =[]
    for x in d:
        if d[x] == v:
            ret.append(x)
    return ret
exec(input().strip())