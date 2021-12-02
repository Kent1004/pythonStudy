list= []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
   for line in f:
      list.append(line[:(line.find(' '))])
max_count = 0
spammer = ''
for ip in list:
    coun_ip = list.count(ip)
    if coun_ip > max_count:
        max_count = coun_ip
        spammer = ip
print (spammer)

