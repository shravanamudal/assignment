# Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension



even_numbers = [x * 2 for x in [1, 2, 3, 4, 5]]
print(even_numbers)




#Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec

import time

def retry(retry_time=3, retry_interval=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(retry_time):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying in {retry_interval} seconds...")
                    time.sleep(retry_interval)
            raise Exception("Maximum retries exceeded.")
        return wrapper
    return decorator

@retry(retry_time=3, retry_interval=3)
def my_function():
    raise Exception("Raise an exception")

my_function()

# Build a counter generator
def counter():
    count = 0
    while True:
        yield count
        count += 1

for count in counter():
    print(count)

