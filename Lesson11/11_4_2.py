class Warehouse:
    EQIN = {}
    SummaryEQ = {}
    def __init__(self,inventory,type,model,location):
        self.location,self.type,self.model,self.inventory = location,type,model,inventory
        if model in self.SummaryEQ: self.SummaryEQ[model]+=1
        else: self.SummaryEQ[model] = 1

    def get_all(self):
        print (self.SummaryEQ)
    def __str__(self):
        return f'{self.inventory} | {self.type} | {self.model}'

class OfficeEquipment(Warehouse):
    def __init__(self,inventory,type, model,location):
        super().__init__(inventory,type,model,location)


class Printer(Warehouse):
    def __init__(self,inventory,model,type,location):
        super().__init__(inventory,type,model,location)


# class Scanner(OfficeEquipment):
#     def __init__(self,type,model, feeder = 'auto'):
#         super().__init__(self.type,self.model)
#         self.feeder = feeder
#         super().__init__(self.feeder)
#
# class Xerox(OfficeEquipment):
#     def __init__(self,type,model, paper_size,paper_slots):
#         super().__init__(self.type,self.model)
#         self.paper_size = paper_size
#         self.paper_slots = paper_slots

pr1 = Printer('00001','HP 426', 'Printer','Sklad1')
# pr2 = Printer('00002','HP 427', 'Printer')
# pr3 = Printer('00003','HP 428', 'Printer')
# pr4 = Printer('00004','HP 429', 'Printer')
# pr5 = Printer('00005','HP 426', 'Printer')

print(pr1)

pr1.get_all()
