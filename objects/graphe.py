import matplotlib.pyplot as plt


class Graphe:
    def __init__(self, counter):
        self.count = counter.get_result()      
        self.res_max = counter.res_max
        self.res_min = counter.res_min  
        self.norm() 

    def norm(self):
        self.abscisse = []
        for i in range(self.res_max - self.res_min + 1):
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

