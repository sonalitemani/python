import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result

    return wrapper

@timer
def sleep(n):
    time.sleep(n)
    return "Done"

sleep(4)


        