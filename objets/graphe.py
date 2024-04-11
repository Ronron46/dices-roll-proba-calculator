import matplotlib.pyplot as plt


class Graphe:
    def __init__(self, compteur):
        self.compte=compteur.compte
        self.abscisse=[]
        for i in range(compteur.res_max-compteur.res_min+1):
            self.abscisse.append(i+compteur.res_min)
    def draw_graph(self):
        plt.bar(self.abscisse,self.compte)
        plt.show()
