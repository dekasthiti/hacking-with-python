from memory_profiler import profile
import timeit

import matplotlib

matplotlib.use('TkAgg')

ITERATIONS = 10000
timer_iterations = 10

@profile
def my_list_with_loop():
    my_list = []
    for i in range(ITERATIONS):
        if i % 2 == 0:
            my_list.append(i)
    return my_list
@profile
def my_list_with_comprehension():
    my_list_comprehension = [i for i in range(ITERATIONS) if i % 2 == 0]
    return my_list_comprehension


def divisible_by_2(i):
    if i % 2 == 0:
        return i
    
@profile
def my_list_with_map():
    my_list_map = list(map(divisible_by_2, range(ITERATIONS)))
    return my_list_map

# or this (much less readable)
# When conditionals don't have an 'else', don't use maps
# def my_list_with_map():
#     my_list_map = list(map(lambda i: i, filter(lambda i: i % 2 == 0, range(ITERATIONS))))
#     return my_list_map
@profile
def my_list_with_filter():
    my_list_filter = list(filter(lambda i: i%2 == 0, range(ITERATIONS)))
    return my_list_filter
@profile
def my_list_with_generator():
    my_list_generator = list(i for i in range(ITERATIONS) if i % 2 == 0)
    return my_list_generator

time = timeit.timeit(my_list_with_loop, number = timer_iterations)
print(f"With loop: {time:>25.3f} seconds")
time = timeit.timeit(my_list_with_comprehension, number = timer_iterations)
print(f"With list comprehension: {time:>11.3f} seconds")
time = timeit.timeit(my_list_with_map, number=timer_iterations)
print(f"With map: {time:>26.3f} seconds")
time = timeit.timeit(my_list_with_generator, number=timer_iterations)
print(f"With generator expression: {time:>9.3f} seconds")


