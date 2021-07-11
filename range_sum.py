"""
Sum of Integers Up To n (integersums.py)

Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.
"""

from functools import reduce


def add_it_up(input):
    if not type(input) is int:
        return 0
    
    if input < 0:
        return reduce(lambda x,y: x+y, range(0, input-1, -1))
    else:
        return reduce(lambda x, y: x+y, range(0, input+1, 1))
    
    
def add_it_up_simple(input):
    if not type(input) is int:
        return 0
    return sum(range(input+1)) if input > 0 else sum(range(0, input-1, -1))


def add_it_up_type_exception(input):
    try:
        return sum(range(input + 1)) if input > 0 else sum(range(0, input - 1, -1))
    except TypeError:
        return 0


def main():
    assert add_it_up('s') == 0, "Non integer inputs should return 0"
    assert add_it_up(0) == 0
    assert add_it_up(10) == sum(range(11))
    assert add_it_up(-1) == sum(range(0, -2, -1))

    assert add_it_up_simple('s') == 0, "Non integer inputs should return 0"
    assert add_it_up_simple(0) == 0
    assert add_it_up_simple(10) == sum(range(11))
    assert add_it_up_simple(-1) == sum(range(0, -2, -1))

    assert add_it_up_type_exception('s') == 0, "Non integer inputs should return 0"
    
    print(f"Range sum to INT_MAX is {add_it_up(Inte)}")
    print(f"Range sum to -1 is {add_it_up(-1)}")


if __name__ == '__main__':
    main()
