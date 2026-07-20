def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(i) for i in args)
        kwargs_values = ', '.join(f'{k}:{v}' for k ,v in kwargs.items())
        print(f"Calling function {func.__name__} with arguments {args_values} and keyword arguments {kwargs_values}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b , c , greet ='dummy'):
    return a + b + c

add(1, 2,3 , greet='hello')