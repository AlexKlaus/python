from functools import wraps


def val_checker(x):
    def _checker(func):
        @wraps(func)
        def wrapper(*args):
            if not x(args[0]):
                msg = f'wrong val {args[0]}'
                raise ValueError(msg)
            else:
                print(func(args[0]))
        return wrapper
    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3


a = calc_cube(5)
