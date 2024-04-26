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
        return tab




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


def diver(n_dice,dice,val_min,mem,tab):
    actual_face = dice
    dice -= 1
    if dice == 0:
        return { actual_face*n_dice : 1}
    else:
        output={}
        for k in range(n_dice+1):
            if (n_dice-k,dice) not in mem:
                mem[n_dice-k,dice]=diver(n_dice-k,dice,val_min,mem,tab)
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


def ui(n_dice,dice):
    mem={}
    tab=[]
    time_start=time.time()
    res=[]
    a=diver(n_dice,dice,n_dice,mem,tab)
    print(a)
    for i in a.keys():
        res.append(a[i])
    timer=time.time() - time_start

    return res, timer, n_dice

def main():
    nb_dice=int(input("combien de dé voulez vous lancez?"))
    dice=int(input("quel est la taille des dés que vous voulez lancer?"))

    count, timer, res_min=ui(nb_dice,dice)

    target=int(input("quel est la cible?"))

    prob=proba(count, target, res_min)

    combi=sum(count)
    print(count)
    print("vous avez", prob*100, "% de chances de reussir" )
    print("il a fallu ", timer, 'secondes pour calculer les', combi, "combinaisons")

