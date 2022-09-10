# Функция hash() и хэши обьэктов для неизменяемых обьэктов
print(hash('Python'))  # для одинаковых обьэктов хэш одинаковые,но это не всегда правильное утверждения!
print(hash('Python'))
print(hash(123))
print(hash((1, 2, 3)))
print('_______')
print('1.Если a==b(равны),то и равен и их хэш.')
a = 1
b = 1
print(a == b)
print('_______')
print('2.Равные hash(c)==hash(b) не гарантируют равенство обьэктов')
print('_______')
print('3.Если хэши не равны hash(e) != hash(d),то обьэкты точно не равны')
e = 1
d = 2
print(hash(e) != hash(d))
print('_____')


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Если определен без метода __hash__ хэш не работает"""
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


point1 = Point(1, 2)
point2 = Point(1, 2)
print(hash(point1), hash(point2), '\n')
