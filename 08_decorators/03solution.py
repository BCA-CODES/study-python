import time

def cache(func):
    cache_args = {}
    print(cache_args)
    def wrapper(*args):
        if args in cache_args:
            return cache_args[args]
        result = func(*args)
        cache_args[args] = result
        return result
    return wrapper


@cache
def example2(a, b):
    time.sleep(4)
    return a + b

print(example2(3,3))
print(example2(3,3))