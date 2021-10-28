import requests
from decimal import *

''' Функция полуения текущего курса по коду валюты '''

def currency_rates (currency):
    '''Получаем курс валют в виде текста'''
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    '''Переводим  код валюты в верхний регистр'''
    currency= currency.upper()
    '''Проверяем наличие кода валюты в полученном запросе'''
    if response.find(currency) == -1:
        print('None')
    else:
        '''ищем начальный индекс курса валюты'''
        begin_position = response.find("<Value>", response.find(currency)) + 7
        '''ищем последний индекс курса валюты'''
        end_position = response.rfind("</Value>", response.find(currency),
                                      response.find("</Valute>", response.find(currency)))
        '''
        возвращаем результат типа Decimal c округлением в копейки ( 2 символа после запятой) путем среза 
        строки запроса по полученым выше индексам начала и конца
        '''
        return Decimal(response[begin_position:end_position].replace(',', '.')).quantize(Decimal("1.00"))



print(currency_rates ("usd"))
print(currency_rates ("eur"))