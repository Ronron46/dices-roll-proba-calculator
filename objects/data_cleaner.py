from objects.dices import Dice


class DataCleaner:
    def __init__(self, data):
        self.data = data
        self.cleaning()
    def cleaning(self):
        self.cleaned_data=self.data.replace(' ','')
        self.cleaned_data=self.cleaned_data.split('+')
        self.res=[]
        for dice in self.cleaned_data:
            self.res.append(dice.split('d'))
        self.res.sort(key=lambda x : int(x[1]), reverse=True)
