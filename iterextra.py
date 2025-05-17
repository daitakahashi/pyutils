
import itertools as it

def repeat_each(iterable, n=1):
    for x in iterable:
        yield from [x]*n

def expand_grid(**kwargs):
    keys = list(kwargs)
    return (dict(zip(keys, values)) for values in it.product(*kwargs.values()))
