# Staicmethod and Classmethod
class Hello:
    def hello_class():
        """Этой функцией может пользоваться только класс!!"""
        print('Hello class!!')

    def hello_example(self):
        """Этой функцией может пользоваться только экземпляр класса!!"""
        print(F'Hello example -->> {self}')

    @staticmethod
    def hello_class_and_example():
        """Теперь этой функцией могут пользоваться как класс
        так и его экземпляр!!!"""
        print('Hello all')

    @classmethod
    def hello_cls(cls):
        """Может пользоваться как клас так и его экземпляр
        но поступать значения будет только класса!!!"""
        print(F'hello -->> {cls}')


example = Hello()
Hello.hello_class()  # Hello class!!
# Hello.hello_example()#TypeError: Hello.hello_example() missing 1 required positional argument: 'self'
print('_______')
Hello.hello_class_and_example()  # Hello all
example.hello_class_and_example() # Hello all
print('_______')
example.hello_example()  # example.hello_example()#
# example.hello_class()#TypeError: Hello.hello_class() takes 0 positional arguments but 1 was given
print('_______')
example.hello_cls() # hello<class '__main__.Hello'>
Hello.hello_cls()  # hello<class '__main__.Hello'>
