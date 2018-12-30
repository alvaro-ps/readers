import operator as op
from inspect import getmembers
from functools import partial

OPERATORS =  {name: func for name, func in getmembers(op) if not name.startswith('__')}

def identity(x):
    return x

def to_set(arg1):
    try:
        set1 = {arg1}
    except TypeError:
        set1 = set(arg1)
    return set1

def issubset(arg1, arg2):
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

OPERATORS['to_set'] = set
OPERATORS['identity'] = identity

class Operation(object):
    def __init__(self, name):
        """
        Returns the operation requested or throw a KeyError if the operation
        is not found. 
        `name` is one of python's operators defined in the `operator` module.
        """
        try:
            self.name = name
            self.operator = OPERATORS[name]
        except:
            available = list(OPERATORS.keys())
            raise KeyError(f'{name} not in the list of possible choices: {available}')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __call__(self, *args, **kwargs):
        return self.operator(*args, **kwargs)
