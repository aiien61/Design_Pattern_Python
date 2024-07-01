import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took up {(end - start)*1_000}ms')
        return result
    return wrapper

def do_something_without_decorator():
    print('Starting...')
    time.sleep(1)
    print('We are done.')
    return True

@time_it
def do_something_using_decorator():
    print('Starting...')
    time.sleep(2)
    print('We are done.')
    return True

if __name__ == '__main__':
    do_something_without_decorator()
    do_something_using_decorator()