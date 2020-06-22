import math
# Exercise 1

class CircleFormula():

    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        di = self.radius * 2
        return di

    def area(self):
        a = math.pi * self.radius**2
        return a

my_circle = CircleFormula(3)
print(my_circle.diameter())
print(f'area of this circle: {my_circle.area()}')

#exercise 2

class MyList():

    def __init__(self):

    def reversed_list(self):
        pass

    def sorted_list(self):
        pass

    def random_list(self):
        pass

