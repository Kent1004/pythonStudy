class Road:
    def __init__(self, length, width):
        self._length =length
        self._width =width
    def massa_road(self):
        return self._length*self._width*25*5

a = Road(20,5000)
print(a.massa_road())
