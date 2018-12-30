"""
Create a `Filter` object that needs to be compiled from a specification, and
that when called on a JSON object, returns a boolean value depending on whether the
object fulfills the constrain imposed by the filter or not.

An specification can be composed of complex queries made of boolean operations among
simple queries.
"""
from .value_getters import ValueGetter
from .operations import Operation

class Filter(object):
    def __init__(self, operator, op1, op2=None, **kwargs):
        """
        - operator: operation name that will be used.
        - op1: jq-like string with the query that fetches the key, which
            will be used as op1.
        - op2: value for the second operand of `operation`.
        - transform: if present apply this function to op1 after getting it
        """
        try:
            self.op1 = Filter(**op1)
        except TypeError:
            try:
                self.op1 = ValueGetter(op1, **kwargs)
            except ValueError as err:
                raise TypeError(f'Error in operand 1: {err}')
        try:
            self.op2 = Filter(**op2)
        except TypeError:
            try:
                self.op2 = ValueGetter(op2, **kwargs)
            except ValueError as err:
                self.op2 = op2
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
        try:
            op2 = self.op2(js)
        except TypeError as err:
            op2 = self.op2

        return self.operator(op1, op2)

    @classmethod
    def fromConfig(cls, config):
        """
        Create a filter from a dict with specifications.
        """
        return cls(**config)
