class Calc_proba:
    def __init__(self, compteur,cible):
        self.res_min=compteur.res_min
        self.compte=compteur.compte
        self.cible=cible
    def proba(self):
        aux=0
        for i in range(len(self.compte)-self.cible+self.res_min):
            aux+=self.compte[i+self.cible-self.res_min]
        return aux/sum(self.compte)
