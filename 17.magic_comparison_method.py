# """Магические методы сравнения!"""


# __eg__   ---- отвечают за ==
# __ne__   ---- отвечают за !=
# __it__   ---- отвечают за <
# __le__   ---- отвечают за <=
# __gt__   ---- отвечают за >
# __ge__   ---- отвечают за >=

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b


b = Rectangle(1,2)
c = Rectangle(1,2)
d = Rectangle(1,3)
print(b == c)#True
print(b == d)#False
