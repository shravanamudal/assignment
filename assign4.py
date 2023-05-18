import time

# Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension



even_numbers = [x * 2 for x in [1, 2, 3, 4, 5]]
print(even_numbers)



# Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec
def retry(retry_time=3, retry_interval=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(retry_time):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    time.sleep(retry_interval)
                    continue
        return wrapper
    return decorator@retry(retry_time=3, retry_interval=3)
def my_function():
    raise Exception("raise an exception")

my_function()



# Build a counter generator

def counter():
    i = 1
    while True:
        yield i
        i += 1
for number in counter():
    print(number)
