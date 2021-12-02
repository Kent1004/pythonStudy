import os
import yaml

'''Рекурсивная функция, обрабатывающая словари и последовательности файла типа yaml
и создающая папки из ключей словаря и папки и файлы из значений 
'''

def rec_creator(*args):
    dict = args[0]
    for key,value in dict.items():
        for val in value:
            if isinstance(val,type(dict)):
               for key1,value1 in val.items():
                  os.makedirs(os.path.join(key, key1), exist_ok=True)
               os.chdir(key)
               rec_creator (val,key1)
               os.chdir('..')
            else:
               os.chdir(key)
               open(val,'w+').close()
               os.chdir('..')


with open("config.yaml", "r") as stream:
    try:
       dict= yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

rec_creator(dict)
