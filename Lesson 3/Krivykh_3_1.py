

def num_translate (number):
    numbers= { 'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'
               }
    print (numbers.get(number))

while True:
    number_input = ''
    num_translate(input(number_input))

