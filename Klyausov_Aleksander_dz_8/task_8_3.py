from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:  # Решение для именованых аргументов
            args += tuple(kwargs.values())
        pos_arg_type = (f'{func.__name__}({arg}: {type(arg)})' for arg in args)  # Тип позиционных
        # аргументов через запятую
        function_type = (f'{func.__name__}({func(arg)}: {type(func(arg))})' for arg in args)  # Тип значения функции
        print(*pos_arg_type, sep=', ')
        print(*function_type, sep=', ')
    return wrapper


@type_logger
def calc_cube(x):
    return x**3


a = calc_cube(4.5, 5, x=10, n=4, number=666)