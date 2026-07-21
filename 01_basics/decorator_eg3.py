from time import sleep
def cache(func):
    cache_values ={}
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper

@cache
def longRunningFunc(a,b):
    sleep(4)
    return a+b

print(longRunningFunc(1,2))
print(longRunningFunc(1,2))
print(longRunningFunc(2,3))