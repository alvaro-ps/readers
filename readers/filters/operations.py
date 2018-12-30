import operator as op
from inspect import getmembers
from functools import partial

OPERATORS =  {name: func for name, func in getmembers(op) if not name.startswith('__')}
OPERATORS['issubset'] = OPERATORS['le']
OPERATORS['issuperset'] = OPERATORS['ge']
OPERATORS['intersects'] = lambda set1, set2: bool(OPERATORS['and_'](set1, set2))
OPERATORS['in'] = lambda value1, set1: OPERATORS['contains'](set1, value1)
OPERATORS['nintersects'] = lambda set1, set2: not OPERATORS['intersects'](set1, set2)
OPERATORS['nin'] = lambda value1, set1: not OPERATORS['intersects'](set1, value1)

class Operation(object):
    def __init__(self, opname):
        """
        Returns the operation requested or throw a KeyError if the operation
        is not found. 
        `opname` is one of python's operators defined in the `operator` module.
        """
        try:
            self.operator = OPERATORS[opname]
        except:
            available = list(OPERATORS.keys())
            raise KeyError(f'{opname} not in the list of possible choices: {available}')

    def __call__(self, *args, **kwargs):
        return self.operator(*args, **kwargs)
