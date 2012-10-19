# -*- coding: utf-8 -*-
import doctest

def calculator(a, b):
    """
    >>> x = calculator(3, 5)
    >>> x
    8
    """
    return a + b


if __name__ == '__main__':
    doctest.testmod()