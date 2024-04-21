# def dices_roll(*args):
#         pools = [tuple(pool) for pool in args]
#         combination = [[]]
#         for pool in pools:
#             combination = [x + [y] for x in combination for y in pool]
#         return combination
# a=[1,2]
# b=[3,4]

# def combi(*args):
#     list=[]
#     res=[0]
#     for i in args:
#         list.append(i)
#     print(list)
#     for dice in list:
#         for y in dice:
#             index=len(res)
#             for x in range(index):
#                 res.append(res[x]+y)
#     return res

# def cartesian_sum(l1,l2):
#     res=[]
#     for x in l1:
#         for y in l2:
#             res.append(x+y)
#     return res


# def rec_sum(*args):
#     result=[0]
#     for dice in args:
#         result=sc(result,dice)
#     return result


# class counter:
#     def __init__(self,depth,max_depth):
#         self.counter=[]
#         self.depth=0
#         self.max_depth=max_depth

# def diver(depth,max_depth, node, dices_list):
#     if depth==max_depth:
#         yield(node)
#     else:
#         for i in dices_list[depth]:
#             yield from diver(depth + 1,max_depth,node + i,dices_list)






from objects.dices import Dice




class DataCleaner:
    def __init__(self, data):
        self.data = data

    def cleaning(self):
        list1 = self.data.split(" ")
        aux = []
        dice_list = []
        for i in list1:
            aux = i.split(",")
            if len(aux) == 2:
                if aux[1] == 'a':
                    dice_list.append(Dice(int(aux[0]) , 'a'))
                elif aux[1] == 'd':
                    dice_list.append(Dice(int(aux[0]), 'd'))
            else:
                dice_list.append(Dice(int(aux[0])))
        return dice_list



class Dice:
    def __init__(self,nb_faces, advantage='non'):
        self.nb_faces = nb_faces
        self.faces = []
        self.advantage = advantage
        self.advantage_verif()

    def advantage_verif(self):
        if self.advantage == 'a':
            for face in range(self.nb_faces):
                for i in range(2 * face + 1):
                    self.faces.append(face + 1)
        elif self.advantage == 'd':
            for face in range(self.nb_faces):
                for i in range(2 * face+1):
                    self.faces.append(self.nb_faces-face)
        elif self.advantage == 'non':
            self.faces = list(range(1, self.nb_faces + 1))



class DiceBucket:
    def __init__(self,dices):
        self.dices = dices
        self.res_min = len(self.dices)
        self.set_dices()
        self.set_res_max()

    def set_dices(self):
        self.dices_list = []
        self.nb_face = []
        for i in self.dices:
            self.dices_list.append(i.faces)
            self.nb_face.append(i.nb_faces)

    def set_res_max(self):
        self.res_max = 0
        for i in self.nb_face:
            self.res_max += i

counter=[]
def create_counter(res_min, res_max):
    global counter
    for i in range(res_max - res_min + 1):
        counter.append(0)


def diver(depth,max_depth, node, dices_list, res_min):
    global counter
    if depth==max_depth:
        counter[node-res_min] += 1
    else:
        for i in dices_list[depth]:
            diver(depth + 1,max_depth,node + i,dices_list,res_min)

class Calc_proba:
    def __init__(self, counter,target,res_min):
        self.res_min = res_min
        self.count = counter
        self.target = target

    def proba(self):
        aux=0
        for i in range(len(self.count) - self.target + self.res_min):
            aux += self.count[i + self.target - self.res_min]
        return aux / sum(self.count)
    def proba_strict_equal(self):
        return self.count[self.target - self.res_min] / sum(self.count)

import time

inp=input("entre ta merde")
time_start=time.time()
liste=DiceBucket(DataCleaner(inp).cleaning())
create_counter(liste.res_min,liste.res_max)
diver(0,len(liste.dices_list),0,liste.dices_list,liste.res_min)
print("il a fallu %s secondes" % (time.time()-time_start))
target=input("oué tu veux cb?")
print("Vous avez ", Calc_proba(counter, int(target),liste.res_min).proba()*100, "% de chance de réussir")

