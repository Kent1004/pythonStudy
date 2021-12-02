import os
import shutil

'''
Скрипт собирает заданные папки и шаблоны в папку template
'''

shutil.rmtree('my_project\\template', ignore_errors=True)
os.chdir('my_project')
for dirpath,dirmidle,files in os.walk(os.getcwd()):
    for file in files:
        if file.rsplit('.',maxsplit=1)[-1] == 'html':
            shutil.copytree( dirpath, 'template\\'+dirpath.rsplit('\\',maxsplit=1)[-1], dirs_exist_ok= True)

