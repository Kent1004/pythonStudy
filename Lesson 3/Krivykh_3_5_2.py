from random import randrange,choice, choices , sample,randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

'''
Функция генерации шуток с повторами по умолчанию:
number - количество шуток
repeat = именованный аргумент : no - без повторов , yes - с повторами
 
'''
def get_jokes(number,repeat='yes'):
    list1=[]
    if number > len(nouns) and repeat == "no":
        print("Введное число превышает максимальное число шуток, равное ", len(nouns))
        number = len(nouns)
        list_nouns = sample(nouns, number)
        list_adverbs = sample(adverbs, number)
        list_adjectives = sample(adjectives, number)
        for i in range(0, number):
            list1.append(f" {list_nouns[i]} {list_adverbs[i]} {list_adjectives[i]}")
    else:
        for i in range(0, number):
            list1.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return print(list1)


get_jokes(6,repeat='no')
get_jokes(6)

