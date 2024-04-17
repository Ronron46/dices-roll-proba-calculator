from objects.dices import Dice, DiceBucket
from objects.counter import Counter
from objects.proba import Calc_proba
from objects.graphe import Graphe
import matplotlib.pyplot as plt
from objects.data_cleaner import DataCleaner


dice_list=input('entrer la liste de dé à lancer, si vous voulez l\'avantage, ajouter un "a" collé au nombre, exemple(4a,3,6,12)...')
clean_dice_list=DataCleaner(dice_list).cleaning()
bucket=DiceBucket(clean_dice_list)
tab=Counter(bucket)
target=input('quelle est la valeur cible?')
print("vous avez ",Calc_proba(tab, int(target)).proba()*100, "% de chance de réussir")

Graphe(tab).draw_graph()
