"""Defines a set of operations to be used within the project. The functionality of this module is exposed
through the class :class:`Operation`. The functions defined here are not meant to be used directly, but
through this class.

The operations can be divided in two categories:

One argument operations
-----------------------
When defining transformations (with the class :class:`Operation <readers.filters.operations.Operation>`). This should
be operations on **one** argument

Two argument operations
-----------------------
When creating filters (with :class:`Filter <readers.filters.filters.Filter>`) with functions applied
on **two** operands, such as :func:`intersects`, :func:`in` or :func:`issuperset` for simple filters :func:`and` or
:func:`or` when creating complex nested filters.


Usage
-----
    >>> from readers.filters.operation import Operation

    >>> #one argument
    >>> op = Operation('len')
    >>> op([1, 2, 3, 4])
    4
    >>> op = Operation('len')
    >>> op('abcde')
    5

    >>> #two arguments
    >>> op = Operation('or')
    >>> op(True, False)
    True
    >>> op = Operation('in')
    >>> op(1, [1, 2, 3])
    True
"""

import operator as op
from inspect import getmembers
from functools import partial

OPERATORS =  {name: func for name, func in getmembers(op) if not name.startswith('__')}

def identity(x):
    """Returns the input"""
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
    """Check whether `arg1` is a superset of `arg2`. Both arguments are converted :func:`to_set`
    before the check.

    :argument arg1:
    :argument arg1:

    Examples:
        >>> issuperset({1, 2}, {1})
        True
        >>> issuperset([1, 2], 1)
        True
        >>> issuperset({3}, {1, 2})
        False
    """
    set1 = to_set(arg1)
    set2 = to_set(arg2)
    return OPERATORS['ge'](set1, set2)

def intersects(arg1, arg2):
    """Check whether the intersection between `arg1` and `arg2` is **non-empty**. Both arguments are
    converted :func:`to_set` before the check.

    :argument arg1:
    :argument arg1:

    Examples:
        >>> intersects({1, 2}, {1})
        True
        >>> intersects([1, 2], 1)
        True
        >>> intersects({3}, {1, 2})
        False
    """
    set1 = to_set(arg1)
    set2 = to_set(arg2)
    return bool(OPERATORS['and_'](set1, set2))

def nintersects(arg1, arg2):
    """Check whether the intersection between `arg1` and `arg2` is **empty**. Both arguments are
    converted :func:`to_set` before the check.

    :argument arg1:
    :argument arg1:

    Examples:
        >>> nintersects({1, 2}, {1})
        False
        >>> nintersects([1, 2], 1)
        False
        >>> nintersects({3}, {1, 2})
        True
    """
    return not intersects(arg1, arg2)

def in_(value1, arg2):
    """Check whether `value1` is included in `arg2`. `arg2` is converted :func:`to_set`
    before the check.

    :argument arg1:
    :argument arg1:

    Examples:
        >>> in_(1, {1, 2, 3})
        True
        >>> in_(1, [1, 2, 3])
        True
        >>> in_(3, {1, 2})
        False

    .. note::
        In order to use this operator with the class :class:`Operation`, the name `in` must be used.

            >>> Operation('in')
            in

        The underscore is appended to avoid name collisions

    """
    set2 = to_set(arg2)
    return OPERATORS['contains'](set2, value1)

def nin_(value1, arg2):
    """Check whether `value1` is **not** included in `arg2`. `arg2` is converted :func:`to_set`
    before the check.

    :argument arg1:
    :argument arg1:

    .. note::
        In order to use this operator with the class :class:`Operation`, the name `nin` must be used.
        The underscore is appended to avoid name collisions

    Examples:
        >>> nin_(1, {1, 2, 3})
        False
        >>> nin_(1, [1, 2, 3])
        False
        >>> nin_(3, {1, 2})
        True
    """
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
        >>> op = Operation('or')
        >>> op(True, False)
        True
        >>> op = Operation('int')
        >>> op('5')
        5
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
        """Returns the operation on the called arguments
        """
        result = self.operator(*args, **kwargs)
        return result
