import sys
from sys import argv

with open('backery.csv', 'r', encoding='utf-8') as f:
    counter = 0
    for line in f:
        counter+=1
        if len(sys.argv) == 2:
            start_line=int(argv[1])
            if (counter == start_line or counter > start_line):
                print(line.strip())
        elif len(sys.argv) == 3:
            start_line = int(argv[1])
            end_line = int(argv[2])
            if counter<=end_line and (counter == start_line or counter > start_line):
                print(line.strip())
        else:
            print(line.strip())









