def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for x in range(len(L)):
        if sum(L[x]) + e <= 100:
            L[x].append(e)
            return True
    else:
        L.append([e])
def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    if len(L) == 0:
        L.append([e])
        return False
    t = [99999999999] * len(L)
    for x in range(len(L)):
        if sum(L[x]) + e <= 100:
            t[x] = 100 -sum(L[x]) - e
    m = min(t)
    if m == 99999999999:
        L.append([e])
        return False
    for x in range(len(L)):
        if t[x] == m:
            L[x].append(e)
    return True
def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    ret = []
    for x in D:
        first_fit(ret,x)
    return ret

def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    ret = []
    for x in D:
        best_fit(ret,x)
    return ret

L=[[95]];best_fit(L,10);print(L)