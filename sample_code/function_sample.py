# -*- coding: utf-8 -*-

# via: https://class.coursera.org/programming1-2012-001/class/index

def area(base, height):                                           # Header
    ''' (number, number) -> number                                # Type Contract
    
    Return the area of a triange with dimensions base             # Description
    and height.
    
    >>> area(10, 5)                                               # Examples
    25.0
    >>> area(2.5, 3)
    3.75
    '''
    
    return base * height / 2                                      # Body