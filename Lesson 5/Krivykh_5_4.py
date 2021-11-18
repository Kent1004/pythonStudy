from sys import getsizeof
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


'''Наивное решение'''
start = perf_counter()
for i in range(0,len(src)-1):
    if i != len(src) and src[i] < src[i+1]:
         result.append(src[i+1])

print('Обычное решение: ',perf_counter() - start , getsizeof (result),'\n' , result)

'''Решение в виде List Comprehensions  улучшает скорость '''
start1 = perf_counter()
result1 = [src [i+1] for i in range(0,len(src)-1)  if i != len(src) and src[i] < src[i+1]]
print('List Comprehensions: ', perf_counter() - start1 , getsizeof (result1), '\n' , result1)

'''Генератор занимает меньше времени и памяти'''
start1 = perf_counter()
result2 = (src [i+1] for i in range(0,len(src)-1)  if i != len(src) and src[i] < src[i+1])
print('Генератор: ',perf_counter() - start1 , getsizeof (result2), '\n' ,list(result2))

# Обычное решение:  9.100011084228754e-06 120
#  [12, 44, 4, 10, 78, 123]
# List Comprehensions:  5.600042641162872e-06 120
#  [12, 44, 4, 10, 78, 123]
# Генератор:  1.2999516911804676e-06 104
#  [12, 44, 4, 10, 78, 123]


