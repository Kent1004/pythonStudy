import os
from os.path import join
dict1 = {}

'''выводит словарь - размер файлов считается от 0 байт'''

folder = 'c:\\windows\\system32'
for n in range(2,6):
    small_files = [file for root, dirs, files in os.walk(folder) for file in files
                   if (os.stat(join(root, file))).st_size >= 0
                   and (os.stat(join(root, file))).st_size < 10 ** n]
    dict1[10**n]=len(small_files) - sum(dict1.values())
print(dict1)


