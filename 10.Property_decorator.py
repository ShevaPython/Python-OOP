# Декоратор Property!Самое главное getter and setter называть одним именем!!!
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def check_balance(self):
        """Декоратор Проперти
        Делаем из функции свойство!!
        Getter по умолчанию """
        return self.__balance

    @check_balance.setter
    def check_balance(self, value):
        """Разширяем функционал свойства!!
        С помощью метода setter!!!"""
        self.__balance = value

    @check_balance.deleter
    def check_balance(self):
        """deliter!!"""
        del self.__balance

vasa = Bank('Vasia',10000)
print(vasa.check_balance) #10000 Обращаемся через свойства!!
print('_______')
vasa.check_balance = 50 #Изменяем через свойства значения self.__balance!
print(vasa.check_balance)#50
print('_______')
del vasa.check_balance
vasa.check_balance = 100000000
print(vasa.check_balance)
print('_______')
del vasa.check_balance # удаления!!
# print(vasa.check_balance)
