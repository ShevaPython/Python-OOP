class Cat:
    breed = 'pers'

    def hello(self):
        print('Hello world wrom kitty')

    def show_breed(self):  # self -->> это наш экземплят класса!
        print(F'may breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):  # проверка на значения name есть ли оно!
            print(F'may name is {self.breed}')
        else:
            print('no name sorry!')  # если такого значиния нету в (instance) то сори!!

    def set_value(self, name, age=10):  # функция создает значения/name/value для экземпляров класса
        self.name = name
        self.age = age


jerrry = Cat()
jerrry.set_value("Jerry")  # передаем значения name и value
print(jerrry.age)
print(jerrry.name)
