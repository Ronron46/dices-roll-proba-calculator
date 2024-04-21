from functions.counter import diver

class Counter:
    def __init__(self, bucket):
        self.counter=[]
        self.res_min=bucket.res_min
        self.res_max=bucket.res_max
        self.dices_list=bucket.dices_list
        self.countdiver()
    
    def countdiver(self):
        for i in range(self.res_max - self.res_min + 1):
            self.counter.append(0)
        aux=diver(0, len(self.dices_list), 0, self.dices_list)
        for i in aux:
            self.counter[i - self.res_min] += 1

    
    



