list= []
with open('nginx_logs_test.txt', 'r', encoding='utf-8') as f:
   for line in f:
      value = (line[:(line.find(' '))],
               line[(line.find('"'))+1:(line.find(' /'))],
               line[(line.find(' /'))+1:(line.find(' HTTP'))])
      list.append(value)
print (list)
