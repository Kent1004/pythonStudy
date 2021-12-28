class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'Car  {self.name} GO '
    def stop(self):
        return f'Car {self.name}  STOP'
    def turn(self, direction):
        self.direction = direction
        if direction == "left": return f' Car turned to left'
        else: return f'Car {self.name} turned to right'
    def show_speed (self):
        return self.speed
    def __str__(self):
        return '{},{},{},{}'.format(self.speed, self.color, self.name, self.is_police)

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} is over speed'

class PoliceCar(Car):
        def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} is over speed'



a= Car (55,'red','HONDA', False)
a1 = TownCar(75,'green','Toyota', False)
a2 = WorkCar(45,'blue','Ford', False)
a3= PoliceCar(80,'white','Lada', True)
a4= SportCar(180,'pink','ZAZ', False)
print (a1,a2,a3,a4,sep='\n')

print(a1.turn('Left'))
print(a2.turn('Right'))
print(a1.show_speed())
print(a2.show_speed())
print(a3.go())
print(a4.stop())
