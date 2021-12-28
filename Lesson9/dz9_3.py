class Worker:
    _income = {"wage": 'wage', "bonus": 'bonus'}
    def __init__(self,name,surname,position):
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):
    def __init__(self,name, surname,position):
        super().__init__(name,surname,position)

    def get_total_income(self):
        return f'{self._income["wage"]} + {self._income["bonus"]}'

    def get_full_name (self):
        return f'{self.surname} {self.name}'

a = Position ('Mike', 'Smith', 'Driver')
print(a.name,a.surname,a.position)
print (a.get_full_name())
print (a.get_total_income())