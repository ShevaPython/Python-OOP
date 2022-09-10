# Магические методы __getitem__,__setitem__,__delitem__
# Предназначены для обращения к обьэкту по индексу!
class Vector:
    def __init__(self, *args):
        self.value = list(args)

    def __repr__(self):
        return str(self.value)

    def __getitem__(self, item):
        """Возвращает индекс обьэкта"""
        if 0 <= item <= len(self.value):  # Проверка на выход из границ нашей колекции!
            return self.value[item]  # Возвращает значения по индексу
        else:
            raise IndexError('Индекс за границей нашей колекции!!')

    def __setitem__(self, key, value):
        """Изменения значения по индексу"""
        if 0 <= key <= len(self.value):  # Проверка на выход из границ нашей колекции!
            self.value[key] = value  # Меняем значения по индексу!!!
        else:
            raise IndexError('Индекс за границей нашей колекции!!')

    def __delitem__(self, key):
        if 0 <= key <= len(self.value):  # Проверка на выход из границ нашей колекции!
            del self.value[key]  # Удаления значения по индексу!
        else:
            raise IndexError('Индекс за границей нашей колекции!!')


vector = Vector(1, 2, 3, 4, 5, 3)
print(vector[0])  # Обращения к нулевому индексу со значением 0
vector[1] = 100000
print(vector)  # [1, 100000, 3, 4, 5, 3] Изменения значения по индексу!
del vector[4]  # Удаления по индексу!!
print(vector)  # [1, 100000, 3, 4, 3]
print('_______')
for i in vector:
    print(i)