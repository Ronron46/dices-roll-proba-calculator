class Counter:
    def __init__(self, bucket):
        self.results = bucket.dices_roll()
        self.count = []
        self.res_min = bucket.res_min
        self.res_max = bucket.res_max
        self.set_result()
    def set_result(self):
        for i in range(self.res_max - self.res_min + 1):
            self.count.append(0)
        for result in self.results:
            self.count[result - self.res_min] += 1
    def get_result(self):
        return self.count
            