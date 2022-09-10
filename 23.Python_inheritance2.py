"""Наследования Ведения"""
# 1.Все в Python являеться обьектом!

# 2.Каждий встроеный тип являеться классом(int,str,float,tuple,dict,set,list...)и они являються подкласом object!
print(issubclass(int, object))  # True


# 3.Любой класс в Python наследуеться от обьекта!!
class Person:  # class Person(object):
    pass  # pass


print(issubclass(Person, object))  # True


class Mylist(list):
    pass


t = Mylist()
# Теперь t Может пользоваться всеми функциями своего родительского класса!!
t.append(22)
print(t)  # [22]
print('_______')


class NewInt(int):
    def repeat(self, value=2):
        """self - это экземпляр класса тоесть наше число!!"""
        return int(str(self) * value)

    def to_bin(self):
        return F'{bin(self)} двоичная система числа{self}'


a = NewInt(9)
print(a.repeat())
d = NewInt(a + 5)
print(d.repeat(3))
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())
