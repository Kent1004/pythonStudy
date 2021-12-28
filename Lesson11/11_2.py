class ZeroError(Exception):
    def __init__(self,message = "Делитель 0!"):
        self.message=message
        super().__init__(self.message)

a = int(input('Введите делимое: '))
b= int(input('Введите делитель:  '))
try:
    if b==0: raise ZeroError()
except ZeroError as err: print(err)
else: print(a/b)

