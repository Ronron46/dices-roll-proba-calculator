# from objects.dices import Dice, DiceBucket
# from objects.counter import Counter
# from objects.proba import Calc_proba
# from objects.graphe import Graphe
# import matplotlib.pyplot as plt
# from objects.data_cleaner import DataCleaner
import time

from functions.diver import diver
from functions.Pascal import pascal
from objects.proba import Calc_proba
from functions.control import control
from objects.data_cleaner import DataCleaner
from functions.zero_counter import zero_counter
from objects.graphe import Graphe

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

dice_list=DataCleaner(data)

count, timer, res_min=control(dice_list.res)
print(res_min)
target=int(input("quel est la cible?"))
combi=zero_counter(sum(count))
graphe=Graphe(count)
prob=Calc_proba(count,res_min,target)
print("vous avez", prob.proba()*100, "% de chances de faire plus que ", target )
print("il a fallu ", timer, 'secondes pour calculer les', combi, "combinaisons")
graphe.draw_graph()

