# Магические методы
class Number:
    def __init__(self, name, many):
        self.name = name
        self.money = many

    """Метод сложения!!"""

    def __add__(self, other):
        return self.money + other

    """Ставит обьэкт на первое место!!"""

    def __radd__(self, other):
        return self + other

    """Метод умножения"""

    def __mul__(self, other):
        return self.money * other

    """Метод вычитания"""

    def __sub__(self, other):
        return self.money - other

    """Метод деления"""

    def __truediv__(self, other):
        return self.money / other


a = Number("Коля", 22)
print(a + 44)  # 66
print(a - 44)  # -22
print(a * 44)  # 968
print(a / 44)  # 0.5
