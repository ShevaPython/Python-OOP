##Наследования Разширения Extending
class Person:
    pass

class Doctor(Person):
    """Extending
    Создания атрибута и методабтакого которого нету в родительском классе
    Расширяя свой функционал!!!"""
    def hello(self):
        print("Привет доктор")
        
