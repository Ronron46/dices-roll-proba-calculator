from objects.dices import Dice


class DataCleaner:
    def __init__(self, data):
        self.data = data
    
    def cleaning(self):
        list1 = self.data.split(" ")
        aux = []
        dice_list = []
        for i in list1:
            aux = i.split(",")
            if len(aux) == 2:
                if aux[1] == 'a':
                    dice_list.append(Dice(int(aux[0]) , 'a'))
                elif aux[1] == 'd':
                    dice_list.append(Dice(int(aux[0]), 'd'))
            else:
                dice_list.append(Dice(int(aux[0])))
        return dice_list