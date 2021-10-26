def row_number(t, e): # return row number of t containing e (top row is row #0)
    for x in range(len(t)):
        if e in t[x]:
            return x
def flatten(t): # return a list of ints converted from list of lists of ints t
    ret = []
    for x in t:
        for y in x:
            if y == 0 :
                continue
            ret+=[y]
    return ret

def inversions(x): # return the number of inversions of list x
    ret = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                ret += 1
    return ret
def solvable(t): # return True if tiling t (list of lists of ints) is solvable
 # otherwise return False
    x = inversions(flatten(t))
    y = row_number(t,0)
    if len(t) %2==1 and x %2 == 0:
        return True
    elif len(t) %2 ==0 and x %2 == 1 and y %2 ==0:
        return True
    elif len(t) %2 ==0 and x %2 == 0 and y %2 ==1:
        return True
        

    return False

print(solvable([[0,1,3,3],[4,8,7,6],[9,10,11,5],[13,12,15,14]]))