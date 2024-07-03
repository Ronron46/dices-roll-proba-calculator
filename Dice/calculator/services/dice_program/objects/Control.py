
from ..functions.adv_list_generator import adv_list_generator
from ..functions.product import product

class Control:
    def __init__(self, dice_list):
        self.dice_list=dice_list.res
        self.adv_list=dice_list.adv_list
        self.starter()
    def simple_calc(self):
        self.res=[]
        self.res_min=0
        for dice in self.dice_list:
            self.res_min += int(dice[0]) 
            dice_faces=[]
            dice_faces=[1]*int(dice[1])
            for i in range(int(dice[0])):
                self.res = product(self.res, dice_faces)
        


    
    def starter(self):
        if len(self.dice_list) !=0:
            self.simple_calc()
        else:
            self.res=[]
            self.res_min=0
        if len(self.adv_list) != 0:
            self.adv_calc()
    def adv_calc(self):
        self.advantage_result=[]
        self.l_adv = adv_list_generator(self.adv_list)
        for adv_dice in self.l_adv:
            self.res_min += adv_dice[0]
            for i in range(adv_dice[0]):
                self.advantage_result = product(self.advantage_result, adv_dice[1])
        self.res=product(self.res,self.advantage_result)
        
        