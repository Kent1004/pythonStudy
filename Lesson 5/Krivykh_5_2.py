import sys
# print (sys.argv[1])
numbers = (num for num in range(1, int(sys.argv[1]) + 1, 2))

'''используется next, чтобы получить истощение генератора , а не for  i in numbers: print (i)'''
for i in range(1, int(sys.argv[1])+1//2):
    print(next(numbers))
