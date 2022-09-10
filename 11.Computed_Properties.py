# Вычисляемые свойства Property
class Square:
    def __init__(self, s):
        self.__said = s
        self.__area = None

    @property
    def said(self):
        """Сделали свойство для возрашения значения площи!!"""
        return self.__said

    @said.setter
    def said(self, value):
        self.__said = value  # Устанавливаем новое значения
        self.__area = None  # Сбрасываем до значения None

    @property
    def area(self):
        """Создаем свойство для вычисления квадрата и кеширования значения"""
        if self.__area is None:
            self.__area = self.__said ** 2
        return self.__area
b = Square(4)
print(b.said)#Вернеться 4 так как getter
b.said = 8 #Устанавливаем новое значения!!
print(b.area)#64 Вычисления с помощтю свойства area!!