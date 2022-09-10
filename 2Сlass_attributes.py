from pprint import pprint
class Person:
    color = None
    name = 'Sergey'
    last_name = 'Shevtsov'
    age = 29

"""Дейстрия над атрибутами класса!!"""
print(Person.name,Person.last_name,Person.age) #Sergey Shevtsov 29

pprint(Person.__dict__)# узнаем все атрибуты класса Person!!!
print(getattr(Person,'name')) #Ecть ли этот атрибут name? вернет Sergey
print(getattr(Person,'x','NO')) #Вернет НО,если нету такого атрибута!

Person.name = 'Misha' # Изменения атрибута на Миша
print(Person.name) #Миша

Person.hobi = "Tenis"
print(Person.hobi) # Tenis,добавлять атрибуты

setattr(Person,'color','yellov') # создавать или заменять атрибуты!
print(Person.color) # yellov

del Person.name # Удаления атрибута!!
delattr(Person,'color') #Удаления атрибута класса!

