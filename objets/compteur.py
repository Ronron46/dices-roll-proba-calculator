class Compteur:
    def __init__(self, bucket):
        self.resultats=bucket.dices_roll()
        self.compte=[]
        self.res_min=bucket.res_min
        self.res_max=bucket.res_max
        for i in range(self.res_max-self.res_min+1):
            self.compte.append(0)
        for resultat in self.resultats:
            self.compte[resultat-self.res_min]+=1
