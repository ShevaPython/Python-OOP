# Слотс,проперти,наследования!
class Rectangle:
    __slots__ = "__width", "height"  # Перечисляем всевозможные атрибуты класса __widh - защещен сразу!

    def __init__(self, a, b):
        self.__width = a
        self.height = b

    @property
    def widht(self):
        return self.__width

    @widht.setter
    def widht(self, value):
        self.__width = value


c = Rectangle(5, 6)
print(c.widht)#5
# print(c.__dict__)#AttributeError: 'Rectangle' object has no attribute '__dict__'. Did you mean: '__dir__'?
""""Наследования"""
print()
class Square(Rectangle):
    """Дочерный клас может добавлять себе свойства методы
    и имеет магический метод __dict__"""
    pass
s = Square(10,20)
print(s.height,s.widht)#20 10
s.color = "red"
print(s.color)#red
print(s.__dict__)#{'color': 'red'} свой метод!!
