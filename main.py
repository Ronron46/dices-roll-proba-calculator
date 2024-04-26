# from objects.dices import Dice, DiceBucket
# from objects.counter import Counter
# from objects.proba import Calc_proba
# from objects.graphe import Graphe
# import matplotlib.pyplot as plt
# from objects.data_cleaner import DataCleaner
import time

from functions.diver import diver
from functions.Pascal import pascal
from functions.proba import proba
from functions.control import control


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

nb_dice=int(input("combien de dé voulez vous lancez?"))
dice=int(input("quel est la taille des dés que vous voulez lancer?"))

count, timer, res_min=control(nb_dice,dice)
target=int(input("quel est la cible?"))
prob=proba(count, target, res_min)
combi=sum(count)
print("vous avez", prob*100, "% de chances de reussir" )
print("il a fallu ", timer, 'secondes pour calculer les', combi, "combinaisons")
