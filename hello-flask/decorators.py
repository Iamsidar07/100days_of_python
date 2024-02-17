# Decorators exercise
import time

current_time = time.time()
print(current_time)


# s since(1st jan 1970)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} took {round(end_time - start_time, 4)}s to run.")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000):
        i * i


fast_function()
slow_function()
