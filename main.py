from objects.dices import Dice, DiceBucket
from objects.counter import Counter
from objects.proba import Calc_proba
from objects.graphe import Graphe
import matplotlib.pyplot as plt
from objects.data_cleaner import DataCleaner
import time


dice_list=input('entrer la liste de dé à lancer, si vous voulez l\'avantage, ajouter un "a" collé au nombre par une virgule, pour un désavantage, mettez un "d". Exemple: 4,a 3 6 12,d...')
start_time=time.time()
clean_dice_list=DataCleaner(dice_list).cleaning()
bucket=DiceBucket(clean_dice_list)
tab=Counter(bucket)
print("--- il a fallu %s secondes ---" % (time.time()-start_time))
target=input('quelle est la valeur cible?')
print("Vous avez ", Calc_proba(tab, int(target)).proba()*100, "% de chance de réussir")
print('Vous avez ', Calc_proba(tab,int(target)).proba_strict_equal()*100, '% de chance d\'obtenir exactement', target)


Graphe(tab).draw_graph()
