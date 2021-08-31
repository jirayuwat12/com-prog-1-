n = int(input())
time_get = {}
all_time_wait = {}
now_q = -1
next_q = 0
def diff_time(f,s):
    return int(f)-int(s)
for _ in range(n):
    i = input()
    if i.startswith('reset'):
        __,t = i.split()
        next_q = int(t)
        now_q = int(t) -1
    elif i.startswith('new'):
        __,t = i.split()
        time_get[next_q] = t
        all_time_wait[next_q] = 0
        print("ticket {0}".format(next_q))
        next_q +=1
    elif i.startswith('next'):
        now_q +=1
        print("call {0}".format(now_q))
    elif i.startswith('order'):
        __,t = i.split()
        all_time_wait[now_q] += diff_time(t,time_get[now_q])
        print("qtime {0} {1}".format(now_q,all_time_wait[now_q]))
    elif i == 'avg_qtime':
        summ = 0
        num = 0
        for x in all_time_wait:
            if all_time_wait[x] != 0:
                summ += int(all_time_wait[x])
                num +=1
        summ /= num 
        print("avg_qtime {0}".format(round(summ,4)))