def thesaurus(*args):
   name_dict = {}
   for name in args:
      if not name[0] in name_dict.keys():
         name_dict[name[0]]= list(name.split())
      else:
         name_dict[name[0]].append(name)
   return name_dict


print (thesaurus("Иван", "Мария", "Петр", "Илья" ,"Света","Миша"))