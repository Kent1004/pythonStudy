from random import randrange,choice, choices , sample,randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

'''Функция генерации шуток из списков'''
def get_jokes(number):
    list1=[]
    for i in range(0,number):
        list1.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return print (list1)

get_jokes(3)
