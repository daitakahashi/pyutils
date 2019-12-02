'''
int_tuple: similar to tuple() but converts values to int
'''

from typing import Iterable, Tuple

def int_tuple(x: Iterable) -> Tuple[int, ...]:
    'integer-tuple constructor'
    return tuple((int(y) for y in x))
