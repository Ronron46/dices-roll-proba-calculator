from objets.dés import Dice, DiceBucket
from objets.compteur import Compteur
from objets.proba import Calc_proba
from objets.graphe import Graphe
import matplotlib.pyplot as plt
from objets.data_cleaner import DataCleaner


liste_dé=input('entrer la liste de dé à lancer, si vous voulez l\'avantage, ajouter un "a" collé au nombre, exemple(4a,3,6,12)...')
liste_dé_propre=DataCleaner(liste_dé).cleaning()
tab=Compteur(DiceBucket(liste_dé_propre))

cible=input('quelle est la valeur cible?')
print("vous avez ",Calc_proba(tab, int(cible)).proba()*100, "% de chance de réussir")

Graphe(tab).draw_graph()
