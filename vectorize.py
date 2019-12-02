'''
similar to an R's Vectorize() function
'''
from typing import Callable, Iterable, Iterator, TypeVar

X = TypeVar('X')
Y = TypeVar('Y')

# sadly enough, I could not find the way to specify
# Callable[[X, *args, ..., **kwargs, ...], Y] and so on.
def vectorize(f: Callable[..., Y]) -> Callable[..., Iterator[Y]]:
    def _f(xs: Iterable[X], *args, **kwargs) -> Iterator[Y]:
        return (f(x, *args, **kwargs) for x in xs)

    return _f

# e.g., int_tuple = lambda x: tuple(vectorize(int)(x))
