list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2=[]
result = ''

for member in list1:
    try:
        mem = int(member)
    except:
        list2.append(member)
        print (member)
        result += ''.join(f'{member} ')
    else:
        for symbol in member:
            if not symbol.isnumeric():
                list2.extend (['"', f'{symbol}{int(member[1:]):02d}','"'])
                result += ''.join(f'"{symbol}{int(member[1:]):02d}" ')
                break
        else:
            list2.extend (['"',f'{int(member):02d}','"'])
            result += ''.join(f'"{int(member):02d}" ')

print(list2)
print(result)

