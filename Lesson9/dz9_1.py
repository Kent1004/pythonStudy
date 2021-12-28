import time
'''
Класс Светофор с защищенным аргументом color и методом running
Атрибут определяет с какого цвета начинает работать светофор циклически
'''
class  TrafficLight:
    def __init__(self,color):
        self._color = color
    def running(self):
        if self._color == 'красный':
            while True:
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
        elif self._color == 'желтый':
            while True:
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
        elif self._color == 'зеленый':
            while True:
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)




a=TrafficLight('желтый')
print (a.running())
