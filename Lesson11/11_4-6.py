class InventoryError(Exception):
    def __init__(self,message = "Инвентарный номер уже закреплен за другим оборудованием"):
        self.message=message
        super().__init__(self.message)
class Warehouse:
    def __init__(self,location):
        self.location = location

class OfficeEquipment(Warehouse):
    '''Словарь - перечень всего оборудования с инвентарными номерами'''
    EQIN = {}
    '''Словарь - остатки оборудования на складе'''
    SummaryEQ = {}
    def __init__(self, inventory_num, model,type, location):
        super().__init__(location)
        self.type=type
        self.model = model
        '''Проверка наличия оборудования с инвентарным номером в словаре с оборудованием и вывод ошибки'''
        if inventory_num in self.EQIN: raise InventoryError()
        else: self.inventory_num = inventory_num
        self.EQIN[inventory_num]=[type, model, location]
        if model in self.SummaryEQ: self.SummaryEQ[model]+=1
        else: self.SummaryEQ[model] = 1


    def __str__(self):
        return f'{self.inventory_num} | {self.type} | {self.model} | {self.location}'
    '''Метод добавления объекта оборудования на склад'''
    def take_eq(self):
        self.location = 'Sklad'
        self.EQIN[self.inventory_num]= [self.type,self.model,self.location]
        return print(f'Устройство ИНВ.{self.inventory_num} принято на склад')

    '''Метод смены расположения объекта оборудования  и вычитание объекта из общего количества на складе'''
    def change_location(self,location):
        self.location = location
        self.EQIN[self.inventory_num] = [self.type,self.model,location]
        self.SummaryEQ[self.model] -= 1
        return print(f'Устройство ИНВ.{self.inventory_num} выдано в отдел {location}')


class Printer(OfficeEquipment):
    def __init__(self,inventory_num,model,type,color='black',location=''):
        super().__init__(inventory_num,model,type,location)
        self.color=color


class Scanner(OfficeEquipment):
    def __init__(self,inventory_num, model,type, feeder = 'auto',location=''):
        super().__init__(inventory_num,model,type,location)
        self.feeder = feeder


class Xerox(OfficeEquipment):
    def __init__(self,inventory_num, model,type, paper_size,paper_slots,location=''):
        super().__init__(inventory_num,model,type,location)
        self.paper_size = paper_size
        self.paper_slots = paper_slots

pr1 = Printer('00001','HP 426', 'Printer','color','Sklad')
pr2 = Printer('00002','HP 429', 'Printer')
sc1= Scanner('00003','Konika 412','Scanner')
sc2= Scanner('00004','Kyocera 1218','Scanner','manual','Sklad')
xerox1 = Xerox('00005','Xerox 1921','Xerox', 'A4/A3','3')

print(pr1.color)
print(pr2.color)
print(sc1.feeder)
print(sc2)
print(xerox1.model,xerox1.paper_size,xerox1.paper_slots,sep=' | ')
print(OfficeEquipment.EQIN)
print(OfficeEquipment.SummaryEQ)
pr1.change_location('Продажи')
pr2.take_eq()
sc1.take_eq()
sc2.change_location('Дирекция')
xerox1.take_eq()
print(OfficeEquipment.EQIN)
print(OfficeEquipment.SummaryEQ)
pr3 = Printer('00001','HP 429', 'Printer')


