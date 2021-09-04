def is_prime(n):
 # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
 if n <= 1:
    return False
 for k in range(2,int(n**0.5)+1):
    if n%k == 0:
        return False
 return True
def next_prime(N):
 # คืนจ านวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N
    N += 1
    while True:
        if(is_prime(N)):
            return N
        N +=1
def next_twin_prime(N):
    N+=1
    while True:
        if is_prime(N) and is_prime(N+2):
            return N,N+2
        N+=1
exec(input().strip())