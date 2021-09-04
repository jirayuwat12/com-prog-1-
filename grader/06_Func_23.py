def make_int_list(x):
 # รับสตริง x มำแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
 # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]
    return [int(i) for i in x.split()]
def is_odd(e):
 # คืนค่ำจริงเมื่อ e เป็นจ ำนวนคี่ ถ้ำไม่ใช่ คืนค่ำเท็จ
    return e%2==1
def odd_list(alist):
 # คืน list ที่มีค่ำเหมือน alist แต่มีเฉพำะตัวที่เป็นจ ำนวนคี่
 # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
    return [int(i) for i in alist if is_odd(int(i))]
def sum_square(alist):
 # คืนผลรวมของก ำลังสองของแต่ละค่ำใน alist
 # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
    return sum([int(i)**2 for i in alist])
exec(input().strip())