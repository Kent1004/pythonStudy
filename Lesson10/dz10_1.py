class Matrix:
    def __init__(self,matrix_list):
        self.matrix_list= matrix_list
    def __str__(self):
        str_matrix = "\n".join(" ".join(map(str, sub)) for sub in self.matrix_list)
        return '{}'.format("\n".join(" ".join(map(str, line)) for line in self.matrix_list))
    '''Сложение только одинаковых по размерам матриц'''
    def __add__(self,other):
        return Matrix([list(map(sum,zip(*i))) for i in zip(self.matrix_list,other.matrix_list)])


a = Matrix([[1,2],[3,4],[5,6]])
b = Matrix([[3,5,32],[2,4,6],[-1,64,-8]])
c= Matrix([[7,8],[9,10],[11,12]])

print (a)
print (b)
print (c)
print (a+c)