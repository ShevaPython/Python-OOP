# Property(проперти) и его методы getter,setter

class Bank:
    def __init__(self, name, balance):
        self.nane = name
        self.__balance = balance

    def get_balance(self):
        """Getter - возвращает значения
        нашего метода self.__balance"""
        print('getter')
        return self.__balance

    def set_balance(self, value):
        """Setter - устанавливаем новое значения self.__balance
        Делаем проверку на числа!"""
        print('setter')
        if not isinstance(value, (int, float)):
            raise ValueError("Это не число,ведите число!!")
        self.__balance = value

    def del_balance(self):
        print('deliter')
        del self.__balance

    # Создаем "Свойство",с помощью которого можно возвращать,заменять,удалать значения self>__balance
    money = property(fget=get_balance, fset=set_balance, fdel=del_balance)


misha = Bank('Misha', 100_000)
print(misha.money)  # 100000 вернет значения срабатывает fget
print('_______')
misha.money = 50  # изменить значения на 50 срабатывает fset
print(misha.money)  # 50
print('_______')
del misha.money
print('_______')
# print(misha.money)#Удалит значения!!Но можем и создать его снова!!
misha.money = 22
print(misha.money)
