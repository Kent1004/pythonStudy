from sys import argv
with open('backery.csv', 'r+', encoding='utf-8') as f:
    change_line = int(argv[1])
    counter = 1
    new_line = argv[2]+'\n'
    # for line in f:
    #     if counter == change_line:
    #        f.write(line.replace(line,new_line))
    #     counter+=1
    lines =f.readlines()
    try:
        lines[change_line-1] = new_line
    except IndexError:
        print('Значение отсутствует')
with open('backery.csv', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    # while counter <= change_line:
    #     line1=f.readline().strip()
    #     print(line1)
    #     if counter == change_line:
    #         #print (type(line1), f.tell())
    #         f.seek(f.tell())
    #         #f.writelines(line1.replace(line1, new_line))
    #         f.writelines(new_line.strip())
    #     counter+=1

    #

    # lines = f.readline()
    # counter = 0
    # new_line = 'new line 12334'
    # for line in f:
    #     counter+=1
    #     if counter == change_line:
    #         print (f.tell())
    #         f.write(new_line)
