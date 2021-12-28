from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def square(self):
        pass


class Suit(Clothes):
    def __init__(self,name,H):
        super().__init__(name)
        self.H= H
    def square(self):
        return f'{self.H*2+0.3}'


class Coat(Clothes):
    def __init__(self,name,V):
        super().__init__(name)
        self.V= V
    @property
    def square(self):
        return f'{self.V/6.5 + 0.5}'


a = Suit('Suit for monkey',10)
print(a.square())
print(a.name)
b= Coat('Coat for dog',56)
print(b.square)
