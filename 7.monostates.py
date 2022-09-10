# Моносостояния для всех экземпляров класса!!!
class Cat:
    # Выбираем словарь,так как он похож на __dict__ key:value и являеться изменяемым!
    __shared_atrr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_atrr  # Подменяем значения дикт! сылаеться на словарь Cat.__shared_atrr


bob = Cat()  # оба имеют атрибут 'pers',and 'black
jon = Cat()
bob.breed = 'black'#Изменяя значения экземпляра класса.будет меняться и в других экземпляров!
print(bob.breed)  # black
print('_______')
print(jon.breed)  # black
