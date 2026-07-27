from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass



class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2



class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width



if __name__ == "__main__":

    shapes = [
        Circle(5),
        Rectangle(4, 5)
    ]


    print("Shape Areas:")

    for shape in shapes:
        print(round(shape.area(), 2))