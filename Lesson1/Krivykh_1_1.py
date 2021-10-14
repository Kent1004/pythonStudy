duration=int(input('Введите секунды: ',))

if duration // 60 == 0:
    print(duration,"сек")
else:
    if duration // 3600 == 0:
        print(duration // 60, "мин", duration % 60, "сек")
    else:
        if duration // (3600*24) == 0:
            print(duration // 3600, "час" , duration % 3600 // 60, "мин" , duration % 3600 % 60, "сек")
        else:
            print(duration // (3600*24),"дн",duration % (3600*24) // 3600, "час", duration % 3600 // 60, "мин", duration % 3600 % 60, "сек")





