def val_checker(callback):
    def val_checker(func):
        def wrapper(*args):
            callback(*args)
            return print(func(*args))
        return wrapper
    return val_checker

def validator(x):
    if x<=0:
        msg = f"wrong val {x}"
        raise ValueError(msg)


@val_checker(validator)
def calc_cube(x):
   return x ** 3

if __name__ == '__main__':
    calc_cube()

