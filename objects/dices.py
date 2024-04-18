
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
    
    def dices_roll(self):
        pools = [tuple(pool) for pool in self.face_number]
        combination = [[]]
        for pool in pools:
            combination = [x + [y] for x in combination for y in pool]  
        result = []
        for i in combination:
            s = 0
            for j in i:
                s += j
            result.append(s)
        return result