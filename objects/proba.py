class Calc_proba:
    def __init__(self, counter,target):
        self.res_min = counter.res_min
        self.count = counter.counter
        self.target = target

    def proba(self):
        aux=0
        for i in range(len(self.count) - self.target + self.res_min):
            aux += self.count[i + self.target - self.res_min]
        return aux / sum(self.count)
    def proba_strict_equal(self):
        return self.count[self.target - self.res_min] / sum(self.count)
