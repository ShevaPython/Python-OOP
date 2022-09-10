#     __slots__
# 1.Мы ограничеваем атрибуты
# 2.Занимаем меньше памяти
# 3.Операции над ними проводяться быстрее!!
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


# p1 = Point(3, 4)
# p1.new_atrr = 10 #ttributeError: 'Point' object has no attribute 'new_atrr'
# print(p1.__dict__)#AttributeError: 'Point' object has no attribute '__dict__'. Did you mean: '__dir__'?
