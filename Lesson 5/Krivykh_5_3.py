from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис','Дмитрий', 'Борис','Дмитрий', 'Борис',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
print('tutors len : ', len(tutors))
print('klasses len : ', len(klasses))

if len(tutors) > len(klasses):
    school = zip_longest(tutors,klasses)
else:
    school = zip(tutors, klasses)

print (type(school), '\n', *school)

'''Проверяем истощение'''
print(next(school))
