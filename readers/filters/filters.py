"""
Create a :class:`Filter` object that needs to be compiled from a specification, and
that when called on a JSON object, returns a boolean value depending on whether the
object fulfills the constrain imposed by the filter or not.

An specification can be composed of complex queries made of boolean operations among
simple queries.

For showing both, the same JSON object will be used:

>>> js = {
...     "key1": [
...         {"key2": 1},
...         {"key2": 2},
...         {"key2": 3}
...     ],
...     "key3": 3
... }

Simple Queries
--------------
We will create a filter that will return ``True`` when ``key3`` is greather than 5.

>>> from readers import Filter
>>> f = Filter(op1='.key3', operator='ge', op2=5)
>>> f(js)
False

Complex Queries
---------------
We will create a filter that will return ``True`` when any of the ``key2`` s in the ``key1`` list
contains the value 2 or ``key3`` equals 7. As this specification is more complex, the :meth:`fromConfig <readers.filters.filters.Filter.fromConfig>` method
will be used.

>>> specs = {
...     "op1": {
...         "op1": ".key1[].key2",
...         "operator": "contains",
...         "op2": 2
...     },
...     "operator": "or",
...     "op2": {
...         "op1": ".key3",
...         "operator": "eq",
...         "op2": 7
...     }
... }
>>> f = Filter.fromConfig(specs)
>>> f(js)
True

A filter can be inspected in an easier way by just prompting it:

>>> f
>>> ((.key1[].key2 - contains - 2) - or - (.key3 - eq - 7))
"""
from .value_getters import ValueGetter
from .operations import Operation

class Filter(object):
    """Creates a filter that will be applied on a JSON object.
    
    :argument operator: operation name that will be used.
    :argument op1: jq-like string with the query that fetches the key, which
        will be used as op1.
    :argument op2: value for the second operand of `operation`.
    :argument transform1: if present apply this function to op1 after getting it
    :argument transform2: if present apply this function to op2 after getting it
    """
    def __init__(self, operator, op1, op2, transform1=None, transform2=None):
        try:
            self.op1 = Filter(**op1)
        except TypeError:
            self.op1 = ValueGetter(op1, transform=transform1)
        try:
            self.op2 = Filter(**op2)
        except TypeError:
            self.op2 = ValueGetter(op2, transform=transform2)
        self.operator = Operation(operator)

    def __str__(self):
        return '(' + ' - '.join([str(self.op1), str(self.operator), str(self.op2)]) + ')'

    def __repr__(self):
        return self.__str__()

    def __call__(self, js):
        """
        Walks the tree and returns the boolean
        """
        op1 = self.op1(js)
        op2 = self.op2(js)

        result = self.operator(op1, op2)

        return result

    @classmethod
    def fromConfig(cls, config):
        """
        Create a filter from a dict with specifications.
        """
        return cls(**config)
