import matplotlib.pyplot as plt


class Graphe:
    def __init__(self, counter):
        self.count = counter.get_result()      
        self.res_max = counter.res_max
        self.res_min = counter.res_min       
    def draw_graph(self):
        self.abscisse = []
        for i in range(self.res_max - self.res_min + 1):
            self.abscisse.append(i + self.res_min)
        plt.bar(self.abscisse,self.count)
        plt.show()
