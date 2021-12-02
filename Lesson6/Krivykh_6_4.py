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
        with open('users_hobbies2.txt', 'w', encoding='utf-8') as f2:
            for line, line1 in zip_longest(f, f1):
                line2 = line.replace("\n","")
                try:
                    line3 = line1.replace("\n","")
                    f2.write(f'{line2}: {line3} \n')
                except AttributeError:
                    f2.write(f'{line2}: None \n')

