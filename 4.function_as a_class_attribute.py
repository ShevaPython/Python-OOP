# Функция как атрибут класса!!!
class Car:
    model = 'BMV'
    engine = 1.6

    @staticmethod
    def drive():#
        print('Lets GO')


Car.drive() #Lets GO
print('________')
getattr(Car,'drive')()   #Lets GO
print('________')
print(Car.__dict__)#'drive': <function Car.drive at 0x0000020658D66710> как функция!!
print('________')

                       #Обращения через экземпляр!!!

a = Car()
print(a.drive)  #<bound method Car.drive of <__main__.Car object at 0x00000234BEC8FA00>>
a.drive()  #Car.drive() takes 0 positional arguments but 1 was given

                          #Можно воспользоваться statickmethod!
print("""class Car:
    model = 'BMV'
    engine = 1.6
    @staticmethod
    def drive():#
        print('Lets GO')""")
print('________')
a.drive() #Lets GO
