import math
from shape import shape

class Circle(shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius
        
    def area(self):
        return 3.141592 * self.__radius * self.__radius
    
    def get_circumference(self):
        return 3.141592 * (self.__radius + self.__radius)