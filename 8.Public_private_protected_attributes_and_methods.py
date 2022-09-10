# Публичные,Защищеные,приватные Атрибуты и методы!!!
class BankAccountPablick:
    """Публичный доступ!Доступны внутри класса и доступны вне класса!!!"""
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print(self.name, self.balance, self.passport)


bob = BankAccountPablick('Bob', 100_000, 45454545)  # Создаем боба с параметрами name,balance,passport
print('Публичный')
bob.print_data()  # Bob 100000 45454545
print(bob.name)  # Публичныебв открытом доступе!!Bob
print(bob.balance)  # Публичныебв открытом доступе!!100000
print(bob.passport)  # Публичныебв открытом доступе!!45454545
print()


class BankAccountProtected:
    """Защищеные атрибуты и методы
    Они все же в открытом доступе,но нужно пользоваться на уровне согласования
    между разработчиками
    Мы должны понимать,что если мы видем (self._)то даный аттрибут лучше не
     использовать вне класса!!!!!!"""

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_data(self):
        print(self._name, self._balance, self._passport)


joni = BankAccountProtected('Joni', 200_000, 534545645)  # Создаем joni  с параметрами name,balance,passport
print('Защищеный')
print(joni._name)
print(joni._balance)
print(joni._passport)
print()


class BankAccountPrivate:
    """Приватные переменные
    Доступ можно получить только через методы
    тоесть нашу фукцию def print_data(self):
    Инкапсуляция данных
    Такжу можно делать и приватные методы!!!"""

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data(self):
        print(self.__name, self.__balance, self.__passport)

    def __print_private_data(self):
        """ Приватный атрибут
        Приватная функция!!"""
        print(self.__name, self.__balance, self.__passport)

    def print_private(self):
        self.__print_private_data()


print('Приватный')
migel = BankAccountPrivate('Migel', 100_000_000, 12424324234)  # Создаем migel  с параметрами name,balance,passport
# print(migel.__name)#AttributeError: 'BankAccountPrivate' object has no attribute '__name'
# print(migel.__balance)
# print(migel.__passport)#AttributeError: 'BankAccountPrivate' object has no attribute '__passport'
migel.print_data()  # Migel 100000000 12424324234
# migel.____print_private_data()#AttributeError: 'BankAccountPrivate' object has no attribute '____print_private_data'
migel.print_private()#Вызов приватной функции  def __print_private_data(self):!!
migel._BankAccountPrivate__print_private_data()#Можно еще получить доступ через класс!!!
print(BankAccountPrivate.__dir__(migel))#Проверка всех атрибутов!!
print(migel._BankAccountPrivate__passport)#12424324234 Пасспорт!!
print(BankAccountPrivate.__dict__.keys())#Для просмотра доступных атрибутов и методов.поможет обратиться к нужному именни!
