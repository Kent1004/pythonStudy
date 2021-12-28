class Stationery:
    def __init__(self,title):
        self.title=title
    def draw(self):
        return f'Запуск отрисовки {self.title} '
class Pen(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        return  f'Запуск отрисовки {self.title} ручкой'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return  f'Запуск отрисовки {self.title} карандошом '

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return  f'Запуск отрисовки {self.title} маркером'

a1=Stationery('Сказка')
a2=Pen('Сказка')
a3=Pencil('Сказка')
a4=Handle('Сказка')
print (a1.draw(),a2.draw(),a3.draw(),a4.draw(),sep='\n')