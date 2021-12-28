class Cell:

    def __init__(self, num_nucleus):
          self.num_nucleus = num_nucleus
    def __str__(self):
        return f'{self.num_nucleus}'

    def __add__(self, other):
        return Cell(self.num_nucleus+other.num_nucleus)
    def __sub__(self, other):
        sub = self.num_nucleus -other.num_nucleus
        return Cell(sub) if sub > 0 else "ErrorMsg: Разность меньше 0"
    def __mul__(self, other):
        return Cell(self.num_nucleus*other.num_nucleus)
    def __floordiv__(self, other):
        return Cell(self.num_nucleus//other.num_nucleus)
    def __truediv__(self, other):
        pass
    def make_order(self,raw):
        self.raw = raw
        return (('*'*self.raw+r'\n')*(self.num_nucleus//self.raw)+'*'*(self.num_nucleus%self.raw))

Cell1 = Cell(126)
Cell2= Cell(24)
print(Cell1+Cell2)
Cell3 = Cell(130)
print(Cell1-Cell3)
print(Cell3-Cell2)
print(Cell2*Cell3*Cell1)
print(Cell1//Cell2)
print(Cell1.make_order(20))
