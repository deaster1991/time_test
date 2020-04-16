from time import time
from functools import wraps


def time_test(func):
    '''
    testing time of func code execution
    from test_time import test_time
    :param func: use @test_time decorator
    :return: func time + func result
    '''

    @wraps(func)
    def wrap(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'func time: {end_time - start_time}')
        return result

    return wrap
