# МНОЖЕСТВЕННОЕ ПРИСВАЕВАНИЯ!!
class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(selfs):
        print("Ура я отучился на доктора")

    def can_build(self):
        print("Я доктор,но я тоже умею строить")


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(selfs):
        print("Ура я отучился на строителя")

    def can_build(self):
        print("Я строитель и я  умею строить")


class Person(Builder, Doctor):
    """При вызове методов и свойств родительский классов
    def graduate and def can_build
    за отсуцтвия своих бутет брать у Builder,
    так как порядок поисков методов начинаеться с него!!"""

    def __init__(self, rank, degree):
        super().__init__(rank)  # Первый метод rank берет у строителя!
        Doctor.__init__(self,
                        degree)  # Что бы взять инициализацию deggre у Doctora,нужно передать обьект и метод,или свойство!


print(Person.__mro__)#(<class '__main__.Person'>, <class '__main__.Builder'>, <class '__main__.Doctor'>, <class 'object'>)
                     #Порядок поиска методов сначала Person - Builder - Doctor - object!

