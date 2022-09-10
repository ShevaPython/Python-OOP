# Магический метод __init__ служит для инициализации, заполнения значений!атрибутов экземпляра класса!!!

class Cat:
    def __init__(self, name='Tom', breed='seams', age=20, color='black'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def hello_cat(self):
        return F'name = {self.name},bread = {self.breed},age = {self.age},color = {self.color} '
# Создаем обьект Tom по стандартным значениям родительского класса!!
tom = Cat()
print(tom.__dict__)  # {'name': 'Vasia', 'breed': 'seams', 'age': 20, 'color': 'black'}
print(tom.hello_cat())
print('_______')
jery = Cat(name='Jery', breed='pers', age=15, color='white')  # Создаем обьект Jery по своим значениям!!
print(jery.__dict__)  # {'name': 'Jery', 'breed': 'pers', 'age': 15, 'color': 'white'}
print(jery.hello_cat())
print('_______')
murzik = Cat('Murzik', 'dvorovoi', 10, 'white')  # Второй способ без именнованых аргументов важен порядок заполнения!
print(murzik.__dict__)#{'name': 'Murzik', 'breed': 'dvorovoi', 'age': 10, 'color': 'white'}
print(murzik.hello_cat())