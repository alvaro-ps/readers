"""
Create a `Filter` object that needs to be compiled from a specification, and
that when called on a JSON object, returns a boolean value depending on whether the
object fulfills the constrain imposed by the filter or not.
"""
from .value_getters import ValueGetter
from .operations import Operation

class Filter(object):
    def __init__(self, op1_getter, operation, op2):
        """
        - op1_getter: jq-like string with the query that fetches the key, which
            will be used as op1.
        - operation: operation name that will be used.
        - op2: value for the second operand of `operation`.
        """
        self.op1_getter = ValueGetter(op1_getter)
        self.operation = Operation(operation)
        self.op2 = op2

    def __call__(self, js):
        """
        Return whether the JSON object passes the filter.
        """
        op1 = self.op1_getter(js)
        return self.operation(op1, self.op2)

    @classmethod
    def fromConfig(cls, specs):
        """
        """
        op1_getter = specs['query']
        operation = specs['operation']
        op2 = specs['value']

        return cls(op1_getter, operation, op2)
