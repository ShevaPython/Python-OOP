# Наследования Делегирования!! Delegation
"""Delegation --- это способ при котором в дочернем классе,можно вызывать
                  метод родительского классая.вызываеться он при помощи
                  super().__init__      super()  -и функция"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return F'Person {self.name} {self.surname}'

    def info(self):
        print("Perent class")
        print(self)


class Dotcor(Person):
    def __init__(self, name, surname, age):
        """Что бы не запутаться с заполнениями даными
        сначала ставим метод super()с инициализацией
        а потом self.age = age!   """
        super().__init__(name,
                         surname)  # Выполняем инициализацию  c помощью родительского класса ,что бы не дублировать код!
        self.age = age

    def __str__(self):
        return F"{self.name} {self.surname}"


person = Person("Ivan", "Ivanov")
doctor = Dotcor("Petr", "Petrov", 22)
print(person.name, person.surname)
print(doctor.name, doctor.surname, doctor.age)
print('_______')
print("Так как,такой функции нету у дочернего класса.Вызываеться родительская! c print('Perent class')")
doctor.info()  # Perent class Petr Petrov
print()
person.info()  # Perent class Person Ivan Ivanov
