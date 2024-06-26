
class Dice:
    def __init__(self,nb_faces, advantage='non'):
        self.nb_faces = nb_faces
        self.faces = []
        self.advantage = advantage
        self.advantage_verif()

    def advantage_verif(self):
        if self.advantage == 'a':
            for face in range(self.nb_faces):
                for i in range(2 * face + 1):
                    self.faces.append(face + 1)
        elif self.advantage == 'd':
            for face in range(self.nb_faces):
                for i in range(2 * face+1):
                    self.faces.append(self.nb_faces-face)
        elif self.advantage == 'non':
            self.faces = list(range(1, self.nb_faces + 1))

        

class DiceBucket:
    def __init__(self,dices):
        self.dices = dices
        self.res_min = len(self.dices)
        self.set_dices()
        self.set_res_max()
    
    def set_dices(self):
        self.face_number = []
        self.nb_face = []
        for i in self.dices:
            self.face_number.append(i.faces)
            self.nb_face.append(i.nb_faces)
    
    def set_res_max(self):
        self.res_max = 0
        for i in self.nb_face:
            self.res_max += i
    
    def cartesian_sum(self,l1,l2):
        res=[]
        for x in l1:
            for y in l2:   
                res.append(x+y)
        return res
            
    def dices_roll(self):
        result=[0]
        for dice in self.face_number:
            result=self.cartesian_sum(result,dice)
        return result
