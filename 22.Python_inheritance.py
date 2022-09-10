"""Наследования Ведения"""


class Person:
    """Базовый класс или родительский!!"""

    def can_breathe(self):
        print("Я могу дышать!")

    def can_walk(self):
        print("Я могу ходить!!")


class Doctor(Person):
    """Это subbclass,или так называемый дочерний класс!!
    который наследует все методы и атрибуты родительского класса Person"""

    def can_cure(self):
        print("Я могу лечить!")


class Arhitec(Person):
    """Это subbclass,или так называемый дочерний класс!!
       который наследует все методы и атрибуты родительского класса Person"""

    def can_build(self):
        print("Я умею строить")


doctor = Doctor()
arhitec = Arhitec()
arhitec.can_build()  # Я умею строить
arhitec.can_breathe()  # Я могу дышать!
arhitec.can_walk()  # Я могу ходить!!
# a.can_cure()#AttributeError: 'Arhitec' не может лечить!
print('_______')
doctor.can_breathe()  # Я могу дышать!
doctor.can_walk()  # Я могу ходить!!
doctor.can_cure()  # Я могу лечить!
# d.can_build()#ttributeError: 'Doctor' не может строить!

"""Проверка являеться ли один класс подкласом другого!!!"""
print(issubclass(Doctor, Person))  # True Являеться ли class Doctor subbclasom Person!
print(isinstance(doctor, Person))  # True
