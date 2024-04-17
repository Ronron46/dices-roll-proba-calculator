class Test:
    def __init__(self):
        self.a=[]
        

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self):
        self__a=[]

class Point:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
