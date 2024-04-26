import time
from functions.diver import diver

def control(n_dice,dice):
    mem={}
    tab=[]
    time_start=time.time()
    res=[]
    a=diver(n_dice,dice,n_dice,mem,tab)
    for i in a.keys():
        res.append(a[i])
    timer=time.time() - time_start

    return res, timer, n_dice