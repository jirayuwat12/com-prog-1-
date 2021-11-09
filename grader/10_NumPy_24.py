import numpy as np
def peak_indexes(x):
    # x เป็นอาเรย์เก็บจ านวนต่าง ๆ
    # คืนอาเรย์ที่เก็บต าแหน่งใน x ที่เป็น "ยอด"
    m = np.append([99999999999999],x[:-1])
    n = np.append(x[1:],[99999999999999999])
    x = (x > m) & (x > n)
    # print(m,n)
    return list(np.where(x == True))[0]
    
def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(', '.join([str(e) for e in pos]))
    else:
        print("No peaks")
exec(input().strip()) # Don't remove this line
# main()