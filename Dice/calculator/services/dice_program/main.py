# from objects.dices import Dice, DiceBucket
# from objects.counter import Counter
# from objects.proba import Calc_proba
# from objects.graphe import Graphe
# import matplotlib.pyplot as plt
# from objects.data_cleaner import DataCleaner
import time


# from functions.control import control
from .objects.Datacleaner import DataCleaner
from .functions.zero_counter import zero_counter
from objects.graphe import Graphe
from objects.control import Control
# dice_list=input('entrer la liste de dé à lancer, si vous voulez l\'avantage, ajouter un "a" collé au nombre par une virgule, pour un désavantage, mettez un "d". Exemple: 4,a 3 6 12,d...')
# time_start=time.time()
# clean_dice_list=DataCleaner(dice_list).cleaning()
# bucket=DiceBucket(clean_dice_list)
# tab=Counter(bucket)
# print("ça a prit", time.time() - time_start, " secondes")
# print(tab.count)
# target=input('quelle est la valeur cible?')
# print("Vous avez ", Calc_proba(tab, int(target)).proba()*100, "% de chance de réussir")
# print('Vous avez ', Calc_proba(tab,int(target)).proba_strict_equal()*100, '% de chance d\'obtenir exactement', target)

# Graphe(tab).draw_graph()

data=input("entre les dés au format '1d4 + 1d8 etc...'")
time_start=time.time()
dice_list=DataCleaner(data)
print(dice_list.res)
control=Control(dice_list)
timer=time.time() - time_start
count = control.res
print(count)
res_min=control.res_min
target=int(input("quel est la cible?"))
combi=zero_counter(sum(count))
graphe=Graphe(count)
prob=Calc_proba(count,res_min,target)
print("vous avez", prob.proba()*100, "% de chances de faire plus que ", target )
print("il a fallu ", timer, 'secondes pour calculer les', combi, "combinaisons")
graphe.draw_graph()

