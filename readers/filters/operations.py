"""Defines a set of operations to be used by the filters created with :class:`readers.filters.filters.Filter`, for both transformations and boolean operations.

The functionality of this module is exposed through :class:`Operation`
"""

import operator as op
from inspect import getmembers
from functools import partial

OPERATORS =  {name: func for name, func in getmembers(op) if not name.startswith('__')}

def identity(x):
    return x

def to_set(arg1):
    """Converts the given argument to a set.

    Examples:
        >>> to_set(1)
        {1}

        >>> to_set([1, 2, 3])
        {1, 2, 3}

    .. warning:: This function does not work with :obj:`range` objects, and maybe some others.
    """
    try:
        set1 = {arg1}
    except TypeError:
        set1 = set(arg1)
    return set1

def issubset(arg1, arg2):
    """Check whether `arg1` is a subset of `arg2`. Both arguments are converted :func:`to_set`
    before the check.

    :argument arg1:
    :argument arg1:

    Examples:
        >>> issubset({1}, {1, 2})
        True
        >>> issubset(1, [1, 2])
        True
        >>> issubset({3}, {1, 2})
        False
    """
    set1 = to_set(arg1)
    set2 = to_set(arg2)
    return OPERATORS['le'](set1, set2)

def issuperset(arg1, arg2):
    set1 = to_set(arg1)
    set2 = to_set(arg2)
    return OPERATORS['ge'](set1, set2)

def intersects(arg1, arg2):
    set1 = to_set(arg1)
    set2 = to_set(arg2)
    return bool(OPERATORS['and_'](set1, set2))

def nintersects(arg1, arg2):
    return not intersects(arg1, arg2)

def in_(value1, arg2):
    set2 = to_set(arg2)
    return OPERATORS['contains'](set2, value1)

def nin_(value1, arg2):
    return not in_(value1, arg2)


OPERATORS['issubset'] = issubset
OPERATORS['issuperset'] = issuperset
OPERATORS['intersects'] = intersects
OPERATORS['nintersects'] = nintersects
OPERATORS['in'] = in_
OPERATORS['nin'] = nin_
OPERATORS['and'] = OPERATORS['and_']
OPERATORS['or'] = OPERATORS['or_']

OPERATORS['float'] = float
OPERATORS['int'] = int
OPERATORS['len'] = len

OPERATORS['to_set'] = to_set
OPERATORS['identity'] = identity

class Operation(object):
    """Creates an operation object from a `name`, that can be then called on the necessary arguments. 

    :argument str name: operator name defined in the :mod:`operator` module or any of the functions
        in this module

    :returns: the operation requested
    :raises KeyError: if the operation is not found

    Examples:
        >>> op = Operation('in')
        >>> op(1, [1, 2, 3])
        True
        >>> op = Operation('len')
        >>> op([1, 2, 3])
        3
    """
    def __init__(self, name):
        try:
            self.name = name
            self.operator = OPERATORS[name]
        except:
            available = list(OPERATORS.keys())
            raise KeyError('{} not in the list of possible choices: {}'.format(name, available))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __call__(self, *args, **kwargs):
        result = self.operator(*args, **kwargs)
        return result
