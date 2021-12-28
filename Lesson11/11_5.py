class Printer():
    def __init__(self,model):
        self.model = model
        self.type= Printer.__name__
    def __str__(self):
        return f'{self.model} , {self.type}'


a = Printer('426')
print(a)

dict = {}
dict1={}
dict['12213'] = ['pr','sdasd']
dict1['3'] = ['22','33']
dict1['3'].append('asdasdasd')


print (dict1)