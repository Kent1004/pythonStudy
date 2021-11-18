from itertools import zip_longest
from sys import exit
with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f1:
        coun_users = sum( 1 for line in f)
        count_hobbies = sum(1 for line in f1)
        if count_hobbies > coun_users:
            exit(1)

with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f1:
        dict = {}
        for line,line1 in zip_longest(f,f1):
            dict[line]=line1

print(dict)

with open('users_hobbies.txt', 'w', encoding='utf-8') as f:
   f.write(dict)

print (dict)