from pprint import pprint
                             #Атрибуты экземпляров классов

class Car:
    model = 'BMV'
    engine = 1.6

pprint(Car.__dict__ ) # все атрибуты класса Car!!

a1= Car()
pprint(a1.__dict__)#Нету методов в нутри экземпляров{}!
a1.color = 'Black'
a1.engine = 2
a1.model = 'Lada'

print(a1.color) #Появился атрибут в нутри экземпляра а1.,больше нигде!
pprint(a1.__dict__)#изменили model,engine,append color внутри а1!и появились свои методы!

a2 = Car()
print(a2.__dict__)#нету своих методов,но можно пользоваться от нашего класса!