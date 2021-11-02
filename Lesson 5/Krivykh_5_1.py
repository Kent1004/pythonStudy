'''
Функция генерирует нечетные числа, возвращает генератор
'''
def odd_num(nume):
    for num in range(1,nume+1,2):
        yield num

if __name__ == '__main__':
    odd_num()