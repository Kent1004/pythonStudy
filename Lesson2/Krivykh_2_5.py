
list1= [57.8, 46.51, 97 , 23.33, 32.2 , 56 , 5 , 548.3, 0.5]
list2=[]
price_list=''
price_list_sort=''
price_list_sort2=''
price_list_sort3=''
# Задание А
for member in list1:
    price_list+= f' {int(str(member).split(".")[0]):02d} руб {str("{:.2f}".format(member)).split(".")[1]} коп,'
print(id(list1), price_list)

#Задание B
list1.sort()
for member in list1:
    price_list_sort+= f' {int(str(member).split(".")[0]):02d} руб {str("{:.2f}".format(member)).split(".")[1]} коп,'
print(id(list1), price_list_sort)

#Задание С

list2 = sorted ( list1 , reverse= True)
for member in list2:
    price_list_sort2+= f' {int(str(member).split(".")[0]):02d} руб {str("{:.2f}".format(member)).split(".")[1]} коп,'
print(id(list2), price_list_sort2)

#  Задание D
for member in list2[4::-1]:
    price_list_sort3+= f' {int(str(member).split(".")[0]):02d} руб {str("{:.2f}".format(member)).split(".")[1]} коп,'
print(id(list2), price_list_sort3)









