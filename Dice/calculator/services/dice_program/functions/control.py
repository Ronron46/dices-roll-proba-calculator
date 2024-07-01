import time
from functions.diver import diver

def control(dice_list):
    mem={}
    tab=[]
    time_start=time.time()
    res=[]
    res_min=0
    for dice in dice_list:
        res_min += int(dice[0]) 
    a=diver(int(dice_list[0][0]),int(dice_list[0][1]),mem,tab,dice_list)
    for i in a.keys():
        res.append(a[i])
    timer=time.time() - time_start

    return res, timer, res_min