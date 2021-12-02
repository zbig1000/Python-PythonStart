from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @property
    def length(self):
        return sqrt(self.x**2 + self.y**2)
    
    @length.setter
    def length(self, new_length):
        if new_length<= 0:
            raise ValueError
        scale = new_length/self.length
        self.x = self.x * scale
        self.y = self.y * scale
        # Your Code Here

v = Vector(3, 4)
print(v.length, v.x, v.y) 

v.length = 10
print(v.length, v.x, v.y)   

v.length = -1
print(v.length, v.x, v.y)   