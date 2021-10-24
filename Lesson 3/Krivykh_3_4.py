"""Функция, возвращающая словарь из Имя-Фамилия """
def thesaurus_adv(*args):
    name_dict = {}
    for name in args:
        name_list=[]
        surname_dict = {}
        if not name.split(' ')[1][0] in name_dict.keys():
            """Проверяем наличия ключа - первой буквы фамилии в словаре, создаем ключ, если  TRUE"""
            if not name.split(' ')[0][0] in surname_dict.keys():
                """
                Проверяем наличия ключа - первой буквы имени во вложенном словаре - и создаем вложенный словарь , если TRUE
                Добавляем Имя-Фамилия во вложенный словарь , если False
                """
                name_list.append(name)
                surname_dict[name.split(' ')[0][0]] = name_list
                name_dict[name.split(' ')[1][0]] = surname_dict
            else:
                name_dict[name.split(' ')[1][0]][name.split(' ')[0][0]].append(name)
        else:
            ''' Добавляем в уже имеющийся ключ  значение Имф-Фамилия взависимости от наличия ключа во вложенном словаре'''
            if not name.split(' ')[0][0] in name_dict[name.split(' ')[1][0]].keys():
                name_list.append(name)
                name_dict[name.split(' ')[1][0]][name.split(' ')[0][0]] = name_list
            else:
                name_list.append(name)
                name_dict[name.split(' ')[1][0]][name.split(' ')[0][0]].append(name)

    return name_dict


print(thesaurus_adv("Иван Дергеев", "Нюра Дмитриева", "Николай Дроздов", "Петр Генич", "Роман Друзь", "Света Иванова", "Миша Губерниев"))
print (thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
