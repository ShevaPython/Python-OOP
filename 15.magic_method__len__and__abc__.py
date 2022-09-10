# МАГИЧЕСКИЕ МЕТОДЫ __len__ and __abc__
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        """Функция вернет суму количества символов!!"""
        return len(self.name + self.surname)


cola = Person("Coca", 'Kolla')
print(len(cola))  # 9
print(cola.__len__())  # 9


class Otrezor:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        # """Нахлждения длины отрезка
        # x2 - x1"""
        return abs(self)  # передаем экземпляр!сработает self.__abc__

    def __abs__(self):
        # """Всегда будет возвращать положительную разницу!"""
        return abs(self.x2 - self.x1)


s = Otrezor(2, 6)
print(len(s))  # 4
print(s.__abs__())  # 4
