import requests , datetime
from decimal import *
from datetime import datetime , date


''' Функция полуения текущего курса по коду валюты '''


def currency_rates(currency):
    '''Получаем курс валют в виде текста'''
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    '''Переводим  код валюты в верхний регистр'''
    currency = currency.upper()
    '''Получем дату в формате date'''
    currency_date = response[(response.find('<ValCurs Date=')+15): (response.find('" name="Foreign Currency Market">'))]
    currency_date = (datetime.strptime(currency_date, "%d.%m.%Y")).date()
    '''Проверяем наличие кода валюты в полученном запросе'''
    if response.find(currency) == -1:
        pass
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
        return f"{Decimal(response[begin_position:end_position].replace(',', '.')).quantize(Decimal('1.00'))}, {currency_date}"
    
if __name__ == '__main__':
    currency_rates()