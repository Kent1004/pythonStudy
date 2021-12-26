import re
'''
Открываем файл с логами,  парсим его и записываем в выходной файл
После сравниваем количество строк в файле, чтобы убедиться ,что все строки исходного файла были обработаны
'''
with open("nginx_logs.txt", "r") as logs:
    with open("nginx_parsed_logs.txt", "w+") as logs_parsed:
        parse = re.compile(r'((?:\d*[.]){3}\d+).+\[(.+)\]."(\w*)\s(/.+/\w*)\s.+"\s(\d+)\s(\d+)')
        for raw in logs:
            logs_parsed.write(f'{"".join(map(str,parse.findall(raw)))}\n')
        '''Сравнение количества строк в исходном в файле и выходном файле'''
        if sum(1 for raw in logs) == sum(1 for raw in logs_parsed):
            print('Количество строк совпадает')



