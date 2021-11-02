src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp = set()
uniq_list = []
for el in src:
   if el not in tmp:
       uniq_list.append(el)
   else:
       try:
           uniq_list.remove(el)
       except ValueError:
           pass
   tmp.add(el)
print(uniq_list)


