# Магические методы __str__ and __repr__

class Lion:
    def __init__(self, name):
        """ВЫзываеться в определеный момент после создания экземпляра класса
        и отвечает за инициализацию!!"""
        self.name = name

    def __repr__(self):
        """Отвечает как будет видить обьэкт разработчик внутри класса"""

        return F'This object Lion - {self.name}'

    def __str__(self):
        """Как будет видить обьэкт пользователь!"""
        return F'Lion - {self.name}'
l = Lion('Simba')
print(l)#Сработал __str__ Lion - Simba
print(str(l))#Сработал __str__ Lion - Simba
l ##Сработал __repr__This object Lion через консоль!
