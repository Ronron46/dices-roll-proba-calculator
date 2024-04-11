from objets.dés import Dice


class DataCleaner:
    def __init__(self, data):
        self.data=data
    def cleaning(self):
        list1=self.data.split(",")
        aux=[]
        liste_dé=[]
        for i in list1:
            aux=i.split("a")
            if len(aux)==2:
                liste_dé.append(Dice(int(aux[0]),True))
            else:
                liste_dé.append(Dice(int(aux[0])))
        return liste_dé
