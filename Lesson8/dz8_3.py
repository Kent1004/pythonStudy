from functools import wraps
''' Декоратор для логирования типов позиционных аргументов'''
def type_logger(func):
    @wraps(func)
    def wrapper (*args,**kwargs):
        if kwargs.items():
            return print(f'{func.__name__}:({", ".join(f"{value}: {type(value)}" for key, value in kwargs.items())})')
        else:
            return print(f'{func.__name__}:({", ".join(f"{arg}: {type(arg)}" for arg in args)})')
    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

if __name__ == '__main__':
    calc_cube()