from objets.dés import Dice, DiceBucket
from objets.compteur import Compteur
from objets.proba import Calc_proba
from objets.graphe import Graphe
import matplotlib.pyplot as plt

a='12'
b=a.split("a")
print(b)
print(int(b[0]))

d=Dice(12)
print(d.faces)