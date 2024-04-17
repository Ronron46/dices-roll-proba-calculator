from objects.dices import Dice


class DataCleaner:
    def __init__(self, data):
        self.data = data
    
    def cleaning(self):
        list1 = self.data.split(",")
        aux = []
        dice_list = []
        for i in list1:
            aux = i.split("a")
            if len(aux) == 2:
                dice_list.append(Dice(int(aux[0]) , True))
            else:
                dice_list.append(Dice(int(aux[0])))
        return dice_list
