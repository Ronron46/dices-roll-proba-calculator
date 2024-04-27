# def pascal(n,k):
#     tab=[]
#     for x in range(n+1):
#         a=[]
#         for y in range(x+1):
#             if y == 0:
#                 a.append(1)
#             elif y == x:
#                 a.append(1)
#             else:
#                 a.append(tab[x-1][y-1] + tab[x-1][y])
#         tab.append(a)
#     return (tab[n][k])

import time


# tab=[]
# def pascal(n,k):
#     time_start=time.time()
#     if n <= len(tab):
#         print("temps : ", time_start - time.time())
#         return (tab[n][k])
#     else:
#         for x in range(len(tab),n+1):
#             a=[]
#             for y in range(x+1):
#                 if y == 0:
#                     a.append(1)
#                 elif y == x:
#                     a.append(1)
#                 else:
#                     a.append(tab[x-1][y-1] + tab[x-1][y])
#             tab.append(a)
#         print("temps : ", time_start - time.time())
#         return(tab[n][k])


# def pascal(n,k,tab):
#     if n <= len(tab):
#         return (tab[n][k])
#     else:
#         for x in range(len(tab),n+1):
#             a=[]
#             if x%2 ==0:
#                 for y in range(int(x/2)+1):
#                     if y == 0:
#                         a.append(1)
#                     elif y == x:
#                         a.append(1)
#                     else:
#                         a.append(tab[x-1][y-1] + tab[x-1][y])
#                 for y in range(x-int(x/2)):
#                     a.append(a[int(x/2)-1-y])
#             elif x%2 != 0:
#                 for y in range(int(x/2)+1):
#                     if y == 0:
#                         a.append(1)
#                     elif y == x:
#                         a.append(1)
#                     else:
#                         a.append(tab[x-1][y-1] + tab[x-1][y])
#                 for y in range(int(x/2)+1):
#                     a.append(a[int(x/2)-y])
#             tab.append(a)
#         return tab[n][k]
def pascal(n,k,tab):
    if n <= len(tab):
        return (tab[n][k])
    else:
        for x in range(len(tab),n+1):
            a=[]     
            for y in range(int(x/2)+1):
                if y == 0:
                    a.append(1)
                elif y == x:
                    a.append(1)
                else:
                    a.append(tab[x-1][y-1] + tab[x-1][y])
            if x%2 ==0:
                for y in range(x-int(x/2)):
                    a.append(a[int(x/2)-1-y])
            elif x%2 != 0:
                for y in range(int(x/2)+1):
                    a.append(a[int(x/2)-y])            
            tab.append(a)
        return tab[n][k]




# mem={}
# def diver(n_dice,dice,val_min):
#     actual_face = dice
#     dice -= 1
#     if dice == 0:
#         return {actual_face * n_dice : 1}
#     else:
#         output={}
#         for k in range(n_dice+1):
#             if (n_dice-k,dice) in mem:
#                 for value, weight in mem[n_dice-k,dice].items():               
#                     value += actual_face *k
#                     weight *= pascal(n_dice,k)
#                     if value in output:
#                         output[value] += weight
#                     else:
#                         output[value] = weight
#             else:
#                 mem[n_dice-k,dice]=diver(n_dice-k,dice,val_min)
#                 for value, weight in mem[n_dice-k,dice].items():

#                     value += actual_face *k
#                     weight *= pascal(n_dice,k)
#                     if value in output:
#                         output[value] += weight
#                     else:
#                         output[value] = weight
#         return  output


# def diver(n_dice,dice,val_min,mem,tab):
#     actual_face = dice
#     dice -= 1
#     if dice == 0:
#         return {actual_face * n_dice : 1}
#     else:
#         output={}
#         for k in range(n_dice+1):
#             mem[n_dice-k,dice]=diver(n_dice-k,dice,val_min,mem,tab)
#             for value, weight in mem[n_dice-k,dice].items():

#                 value += actual_face *k
#                 weight *= pascal(n_dice,k,tab)
#                 if value in output:
#                     output[value] += weight
#                 else:
#                     output[value] = weight
#         return  output

from objects.proba import Calc_proba
from objects.graphe import Graphe




# def diver(n_dice,dice,val_min,mem,tab):
#     actual_face = dice
#     dice -= 1
#     if dice == 0:
#         return {actual_face * n_dice : 1}
#     else:
#         output={}
#         for k in range(n_dice+1):
#             if (n_dice-k,dice) in mem:
#                 for value, weight in mem[n_dice-k,dice].items():               
#                     value += actual_face *k
#                     weight *= pascal(n_dice,k,tab)
#                     if value in output:
#                         output[value] += weight
#                     else:
#                         output[value] = weight
#             else:
#                 mem[n_dice-k,dice]=diver(n_dice-k,dice,val_min,mem,tab)
#                 for value, weight in mem[n_dice-k,dice].items():
#                     value += actual_face *k
#                     weight *= pascal(n_dice,k,tab)
#                     if value in output:
#                         output[value] += weight
#                     else:
#                         output[value] = weight
#         print(mem)
#         return  output


def diver(n_dice,dice,mem,tab,dice_list):
    aux_list=dice_list.copy()
    actual_face = dice 
    if len(aux_list) >=2:
        if int(aux_list[1][1]) == actual_face:
            n_dice += int(aux_list[1][0])
            aux_list.pop(1)   
    dice -= 1
    if dice == 0:
        return { actual_face*n_dice : 1}
    else:
        output={}
        for k in range(n_dice+1):
            if (n_dice-k,dice) not in mem:
                mem[n_dice-k,dice]=diver(n_dice-k,dice,mem,tab,aux_list)
            for value, weight in mem[n_dice-k,dice].items():
                value += actual_face *k
                weight *= pascal(n_dice,k,tab)
                if value in output:
                    output[value] += weight
                else:
                    output[value] = weight
        return  output


def proba(count, target, res_min):
    aux=0
    for i in range(len(count) - target + res_min):
        aux += count[i + target - res_min]
    return aux/sum(count)


class DataCleaner:
    def __init__(self, data):
        self.data = data
        self.cleaning()
    def cleaning(self):
        self.cleaned_data=self.data.replace(' ','')
        self.cleaned_data=self.cleaned_data.split('+')
        self.res=[]
        for dice in self.cleaned_data:
            self.res.append(dice.split('d'))
        self.res.sort(key=lambda x : int(x[1]), reverse=True)


def ui(dice_list):
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


test_list=[]
for i in range(100):
    test_list.append(2*i+1)





def main():
    data=input("entre les dés au format '1d4 + 1d8 etc...'")
    time_oi=time.time()
    dice_list=DataCleaner(data)
    count, timer, res_min=ui(dice_list.res)
    res=[]
    for i in range(len(test_list)+len(count)-1):
        res.append(0)

    # target=int(input("quel est la cible?"))

    # prob=proba(count, target, res_min)
    print(len(count),len(test_list))
    # combi=sum(count)
    # print(count)
    # print("vous avez", prob*100, "% de chances de reussir" )
    # print("il a fallu ", timer, 'secondes pour calculer les', combi, "combinaisons")
    for x in range(len(count)):
        for y in range(len(test_list)):
            res[x+y] += count[x]*test_list[y]
    print("ça a prit : ",time.time() - time_oi)
    graphe=Graphe(res)
    graphe.draw_graph()

    

