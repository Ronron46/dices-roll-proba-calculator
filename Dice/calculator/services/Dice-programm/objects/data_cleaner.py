from functions.rec_pop import rec_pop
class DataCleaner:
    def __init__(self, data):
        self.data = data
        self.cleaning()
    def cleaning(self):
        self.adv_list=[]
        self.cleaned_data=self.data.replace(' ','')
        self.cleaned_data=self.cleaned_data.split('+')
        self.res=[]
        for dice in self.cleaned_data:
            self.res.append(dice.split('d'))
        self.aux=self.res.copy()
        rec_pop(self.res,self.adv_list)
        self.res.sort(key=lambda x : int(x[1]), reverse=True)
