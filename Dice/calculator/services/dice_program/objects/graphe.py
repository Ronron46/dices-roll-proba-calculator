import matplotlib.pyplot as plt


class Graphe:
    def __init__(self, count):
        self.count = count
        self.res_min=self.count[0] 
        self.norm()

    def norm(self):
        self.abscisse = []
        for i in range(len(self.count)):
            self.abscisse.append(i + self.res_min)
        self.ordinate = []
        self.count_sum = sum(self.count)
        self.verif=0
        for i in self.count:
            self.ordinate.append(i / self.count_sum)
            self.verif += (i / self.count_sum)

    def draw_graph(self):   
        plt.bar(self.abscisse,self.ordinate)
        plt.show()

