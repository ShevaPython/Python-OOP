#### Декоратот total_ordening Для разширения функционала Сравнения!!
from functools import total_ordering
@total_ordering
class BancAccount:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


ac1 = BancAccount(20)
ac2 = BancAccount(10)
print(ac1 == ac2)
print(ac1 < ac2)
print(ac1 > ac2)
print(ac1 != ac2)
print(ac1 <= ac2)
print(ac1 >= ac2)
# False
# False
# True
# True
# False
# True
