"""
Decorators are functions that wrap around other functions

The wrapped function's functionality can be extended (adding timer start/stop around this function(
, modified (choose to return / don't return the function's results, modify the function's inputs etc)
or for that matter, conditionally executed.

Wrapper registration functions also functions to register themselves at compile time (see example)
"""

import sys
import random

# Global PLUGINS dictionary
PLUGINS = dict()


def register(func):
    """
    This example is taken from https://realpython.com/primer-on-python-decorators/
    :param func:
    :return:
    """
    PLUGINS[func.__name__] = func
    
@register
def say_hello(name):
    print(f"Hello {name}!")
    print("Nice to meet you!")

@register
def say_goodbye(name):
    print(f"Goodbye {name}!")
    
    
import functools
import time


def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
    
    
import math

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(100)])
    
def main(argv):
    greeter, greeting = random.choice(list(PLUGINS.items()))
    print(f"We picked {greeter}")
    
    greeting(argv[0])
    
    print("Start countdown")
    countdown(10)
    
    # print("Print debug info")
    # approximate_e()
    #

    waste_some_time(3)
    

if __name__ == '__main__':
    main(sys.argv[1:])