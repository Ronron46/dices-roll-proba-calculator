class Calc_proba:
    def __init__(self, count,res_min,target):
        self.res_min = res_min
        self.count = count
        self.target = target

    def proba(self):
        aux=0
        for i in range(len(self.count) - self.target + self.res_min):
            aux += self.count[i + self.target - self.res_min]
        return aux / sum(self.count)
    def proba_strict_equal(self):
        return self.count[self.target - self.res_min] / sum(self.count)
