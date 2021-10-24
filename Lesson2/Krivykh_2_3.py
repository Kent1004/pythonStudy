list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = ''
i = 0
while list1 [i] != list1[len(list1)-1]:
    try:
        mem = int(list1[i])
    except:
        result += ''.join(f'{list1[i]} ')
        i+=1
    else:
        for symbol in list1[i]:
            if not symbol.isnumeric():
                list1.insert(i,'"')
                list1.insert(i+1, f'{symbol}{int(list1[i+1][1:]):02d}')
                list1.insert(i+2, '"')
                list1.pop(i+3)
                result += ''.join(f'"{symbol}{int(list1[i+1][1:]):02d}" ')
                i+=3
                break
        else:
            list1.insert(i, '"')
            list1.insert(i + 1, f'{int(list1[i+1]):02d}')
            list1.insert(i + 2, '"')
            list1.pop(i+3)
            result += ''.join(f'"{int(list1[i+1]):02d}" ')
            i+=3
else:
     result+=list1[len(list1)-1]
print(list1)
print( result)

