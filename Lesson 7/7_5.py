import os
import json
from os.path import join
dict1 = {}

'''выводит словарь - размер файлов считается от 0 байт до 100000 байт и список расширений файлов в данном иапазоне значений '''

folder = 'c:\\windows\\system32'
for n in range(2,6):
    small_files = [file.rsplit('.',maxsplit=1)[-1] for root, dirs, files in os.walk(folder) for file in files
                   if (n != 2 and (os.stat(join(root, file))).st_size >= 10**(n-1)
                   and (os.stat(join(root, file))).st_size < 10 **n )
                   or (n == 2 and (os.stat(join(root, file))).st_size >= 0
                       and os.stat(join(root, file)).st_size < 10 **n)]
    dict1[10**n]=(len(small_files),(list(set(small_files))))

json_dict1 = json.dumps(dict1)
with open(folder.rsplit('\\',maxsplit=1)[-1]+'_summary.json', 'w', encoding='utf-8') as f:
   f.write(json_dict1)






