#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_03"""


def bool_to_str(bval):
    """This function does some evaluation.

    Args:
        bval(mixed): Arg to take value and compare it with function statements.
    Returns:
        str: 'Yes' if bval is truthy and 'No' if bval is falsy.
    Examples:
        >>> bool_to_str(True)
        'Yes'
        >>> bool_to_str('')
        'No'
    """
    if bval:
        answ = 'Yes'
    else:
        answ = 'No'
    return answ
