list_nechetnye = []

list_sum = 0 # Сумма чисел, сумма цифр которых равна 7
list_sum2 = 0 # Сумма  чисел , сумма цифр которых равна 7 , с арифметическим прибавлением 17
list_sum3 = 0 # Сумма  чисел , сумма цифр которых равна 7 , с добавлением в конце  каждого элемента листа цифр 17
for i in range (1,1000):
    if i % 2:
        list_nechetnye.append(i ** 3)
#Задание a
for number in list_nechetnye:
    number_variable = number
    number_sum = 0
    while number_variable != 0 :
        number_sum += number_variable % 10
        number_variable = number_variable // 10
    if number_sum % 7 == 0:
        list_sum += number
print("Задание а  - сумма чисел, сумма цифр которых кратно 7:  ",list_sum)

#Задание b с арифметическим прибавлением 17

for number in list_nechetnye:
    number += 17
    number_variable = number
    number_sum = 0
    while number_variable != 0 :
        number_sum += number_variable % 10
        number_variable = number_variable // 10
    if number_sum % 7 == 0:
        list_sum2 += number
print("Задание b   - сумма чисел + 17, сумма цифр которых кратно 7:  ",list_sum2)

#Задание b с добавлением в конце  каждого элемента листа цифр 17

for number in list_nechetnye:
    number = str(number)+'17'
    number = int(number)
    number_variable = number
    number_sum = 0
    while number_variable != 0 :
        number_sum += number_variable % 10
        number_variable = number_variable // 10
    if number_sum % 7 == 0:
        list_sum3 += number
print("Задание b   - сумма чисел c добавлением 17, сумма цифр которых кратно 7:  ",list_sum3)



