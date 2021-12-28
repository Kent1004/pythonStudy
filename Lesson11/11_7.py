class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        if self.b < 0 : return f'{self.a}{self.b}i'
        elif self.b == 0: return f'{self.a}'
        elif self.b>0: return f'{self.a}+{self.b}i'

    def __add__(self, other):
        return Complex((self.a+other.a),(self.b+other.b))

    def __sub__(self, other):
        return Complex((self.a - other.a), (self.b - other.b))

    def __mul__(self, other):
        return Complex((self.a * other.a - self.b*other.b), (self.a*other.b +  self.b*other.a))


cpx1 = Complex(3,5)
cpx2 = Complex(-7,-12)
cpx3 = Complex(7,12)
print (cpx1)
print (cpx2)
print (cpx3)
print('Сложение:',cpx1+cpx2)
print ('Вычитание:',cpx1-cpx2)
print ('Умножение:', cpx1*cpx2)
print('Сложение:',cpx1+cpx3)
print ('Вычитание:',cpx1-cpx3)
print ('Умножение:', cpx1*cpx3)

