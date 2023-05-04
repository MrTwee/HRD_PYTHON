from abc import *

class Shape(metaclass=ABCMeta):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def move(self, offset_x, offset_y):
        self.__x += offset_x
        self.__y += offset_y

    @abstractmethod
    def area():
        pass

import math
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self. __width = width
        self. __height = height

    def area(self):
        return self.__width * self.__height
    
    def get_diagonal(self):
        return math.sqrt(self.__width * self.__width + self.__height * self.__height)

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius
        
    def area(self):
        return 3.141592 * self.__radius * self.__radius
    
    def get_circumference(self):
        return 3.141592 * (self.__radius + self.__radius)
    
def printArea(shape):
    if type(shape) == Rectangle:
        s = "circle diagonal: "
        s += f"{shape.get_diagonal():.2f}"
    elif type(shape) == Circle:
        s = "circle circumference: "
        s += f"{shape.get_circumference()}"
    else:
        pass

    print(s, "area:", shape.area())

shapes = [
    Rectangle(10, 10, 5 ,20), Circle(50, 50, 5), Rectangle(0, 0, 100, 5), Rectangle(50, 50, 5, 20)
]

for shape in shapes:
    printArea(shape)