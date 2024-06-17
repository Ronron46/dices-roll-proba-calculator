import matplotlib.pyplot as plt
from calculator.services.dice_program.functions.zero_counter import zero_counter


class Graph:
    def __init__(self, count,res_min):
        self.count = count
        self.res_min=res_min 
        self.norm()

    def norm(self):
        self.combi=sum(self.count)
        for i in range(len(self.count)):
            self.count[i]/=self.combi
            self.count[i]*=100
        self.total_comb = zero_counter(self.combi)
        self.abscisse = []
        for i in range (len(self.count)):
            self.abscisse.append(i+self.res_min)
        self.less=[]
        for i in range(len(self.count)):
            if i ==0:
                self.less.append(self.count[i])
            else:
                self.less.append(self.less[i-1]+self.count[i])
        self.more=[]
        for i in range(len(self.count)):
            if i==0:
                self.more.append(100)
            else:
                self.more.append(self.more[i-1]-self.count[i-1])
    
    def data(self):
        return self.abscisse, self.count, self.less, self.more, self.total_comb