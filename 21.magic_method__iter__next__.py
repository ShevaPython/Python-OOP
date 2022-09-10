# Магический метод __iter__,__next__
class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    # def __iter__(self):
    #     """Метод итер с встроеным функцией __Next__ внутри str(self_name)
    #     А не в нутри нашего метода!!"""
    #     return iter(self.marks)
    def __iter__(self):
        """Делаем свой итератор!!"""
        self.start = 0  # Создаем индекс со значением старт 0!!!
        self.stop = len(self.name) - 1  # Создаем индекс последнего элемента!!

        return self  # экземпляр!

    def __next__(self):
        """Аналог цыкла while self.start += 1"""
        if self.start > self.stop:  # Eсли индекс 1 элемента больше индекса 2 элемента!
            raise StopIteration
        letter = self.name[self.start]  # Сохраняем индекс 1 вого элемента в переменной Letter!
        self.start += 1  # Увеличиваем индекс наш старт на 1!
        return letter


igor = Student("Igor", "Nicolaev", [1, 4, 2, 3, 1, 2])
for i in igor:
    print(i)
