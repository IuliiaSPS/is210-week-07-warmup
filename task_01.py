#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


def fibonacci(maxint):
    """This function returns Fibonacci sequence.

    Args:
        maxint(int): upper bound value to be arithmetically calculated.
    Returns:
        list: every number after the first two is the sum of the preceding ones.
    Examples:
        >>>fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
        >>>fibonacci(99)
        [0, 1, 1, 2, 3, 5, 8]
    """
    first_val, second_val = 0, 1
    fibonacci_list = [0]
    while second_val < maxint:
        fibonacci_list.append(second_val)
        first_val, second_val = second_val, first_val+second_val
    return fibonacci_list
