import numpy as np

def f1(x):
    s = x[:-1]
    t = x[1:]
    temp = t/s
    return sum(np.isclose(temp[0],temp)) == x.shape[0]-1

def f2(x):
    y = np.array(x)
    y[:,:-1] += x[:,1:]
    y[:,:-2] += x[:,2:]
    y[:,:-2] /= 3.0
    y[:,-2:-1] /= 2.0
    return y

def checkN(x,t = 1):
    all_sum = np.sum(x)
    if t == 0:
        all_sum = x.shape[0] **2 -all_sum
    x = x == t
    t_sum = np.sum(x[:,0]) + np.sum(x[:,-1]) + np.sum(np.diag(x)) - x[0,0] - x[-1,-1]
    if all_sum == t_sum and all_sum == x.shape[0]*3 -2:
        return True
    return False

def f3(x):
    if x.shape == (1,1):
        return True
    #1
    stt =  checkN(x) or checkN(x[:,::-1]) or checkN(x.T) or checkN(x.T[:,::-1])
    #0
    return stt or checkN(x,0) or checkN(x[:,::-1],0) or checkN(x.T,0) or checkN(x.T[:,::-1],0)
    
print(f2(np.array([[9.5]])))