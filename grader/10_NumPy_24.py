import numpy as np
def peak_indexes(x):
    # x เป็นอาเรย์เก็บจ านวนต่าง ๆ
    # คืนอาเรย์ที่เก็บต าแหน่งใน x ที่เป็น "ยอด"
    ret = []
    if x[0] > x[1]:
        ret.append(0)
    if x[-2] > x[-1]:
        ret.append(len(x)-1)
    i = 1
    while i < len(x)-1:
        if x[i-1] < x[i] and x[i] > x[i+1]:
            ret.append(i)
        i += 1
    return ret 
def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")
exec(input().strip()) # Don't remove this line
