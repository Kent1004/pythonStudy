from datetime import datetime
class Data:
    def __init__(self,dat):
        self.dat=dat
    @staticmethod
    def validate(data):
        try:
            datetime.strptime(data, '%d-%m-%Y')
        except:
            print ("Дата не валидна")
        else:
            print("Дата валидна")

    @classmethod
    def is_integer(cls,param):
        date,mounth,year = map(int,param.split('-'))
        return date,mounth,year

    def __str__(self):
        return self.dat


a = Data ('01-02-1999')
print (Data.is_integer('01-02-1988'))
a.validate('30-02-1999')
a.validate('27-02-1999')

