# Полиморфизм --это возможность обработки совершенно разных обьэктов путем
# использованию одного и тогоже метода по названию,а так же при помощи магических методов пример__str__

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle {self.a} x {self.b} ="


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2

    def __str__(self):
        return F"Square {self.a} x {self.a} ="


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2

    def __str__(self):
        return F'Circle r  {self.r} ='

rec1 = Rectangle(2,4)
rec2 = Rectangle(3,10)
sq1 = Square(5)
sq2 = Square(8)
cir1 = Circle(5)
cir2 = Circle(8)
figures = [rec1,rec2,sq1,sq2,cir1,cir2]
for figure in figures:
    print(figure,figure.get_area())
"""Rectangle 2 x 4 = 8
Rectangle 3 x 10 = 30
Square 5 x 5 = 25
Square 8 x 8 = 64
Circle r  5 = 78.5
Circle r  8 = 200.96"""