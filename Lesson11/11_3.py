class InputError(Exception):
    def __init__(self,message = "Вы ввели не число!"):
        self.message=message
        super().__init__(self.message)
list = []
elm= ''
while elm != 'stop':
    try:
        elm = input('Введите данные: ')
        if not elm.isdigit(): raise InputError()
    except InputError as er: print(er)
    else: list.append(int(elm))
print (list)




