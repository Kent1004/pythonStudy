
def num_translate_adv (number):
    numbers= { 'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять' }
    number_upp = ''
    if number[0].isupper():
        number_upp = numbers.get(number.lower())
        print (number_upp.capitalize())
    else:
        print (numbers.get(number))

number_input = ''
num_translate_adv(input(number_input))

