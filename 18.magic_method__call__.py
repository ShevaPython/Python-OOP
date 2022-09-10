from time import perf_counter


# Магический метод __Call__-вызов!
# 1 ПРИМЕР ИСПОЛЬЗОВАНИЯ В КАЧАСТВЕ ЗАМЫКАНИЯ!!!
class Counter:
    def __init__(self):
        self.counter = 0
        self.suma = 0
        self.lenght = 0

    def __call__(self, *args, **kwargs):
        """Делает замыкания для каждого экземпляра класса отдельно!!"""
        self.counter += 1
        self.suma += sum(args)
        self.lenght += len(args)

    def average(self):
        """Нахождения среднего арифметического"""
        return self.suma / self.lenght


a = Counter()
b = Counter()
print(a.counter, a.suma, a.lenght)  # 0 0 0
a(1, 2, 3, 4, 5)
print(a.counter, a.suma, a.lenght)  # вызывалась функция - 1  сума чмсел -15 количество - 5
print(b.counter, b.suma, b.lenght)  # 0 0 0
b(2, 3, 4)
print(b.counter, b.suma, b.lenght)  # 1 9 3
print('_______')


# Использовать в качестве декоратора!!!from time import perf_counter
class Timer:
    def __init__(self, funk):
        self.fk = funk

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(F'Вызываеться функция {self.fk.__name__}')
        result = self.fk(*args, **kwargs)
        finish = perf_counter()
        print(F'Функция отработала за {finish - start}')
        return result


# @Timer
def fact(n):
    col = 1
    for i in range(1, n + 1):
        col *= i
    return col


fact = Timer(fact)
fact(5)  # Вызываеться функция fact 89N3PDyZzakoH7W6n8ZrjGDDktjh8iWFG6eKRvi3kvpQ
# Или же с помощью декоратора Timer
