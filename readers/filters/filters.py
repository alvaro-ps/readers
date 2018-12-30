"""
Create a `Filter` object that needs to be compiled from a specification, and
that when called on a JSON object, returns a boolean value depending on whether the
object fulfills the constrain imposed by the filter or not.
"""
from .value_getters import ValueGetter
from .operations import Operation

class Filter(object):
    def __init__(self, operation, op1, op2, transform=None):
        """
        - op1_getter: jq-like string with the query that fetches the key, which
            will be used as op1.
        - operation: operation name that will be used.
        - op2: value for the second operand of `operation`.
        - transform: if present apply this function to op1 after getting it
        """
        self.op1_getter = ValueGetter(op1, transform)
        self.operation = Operation(operation)
        self.op2 = op2

    def __str__(self):
        return " - ".join([str(self.op1_getter), str(self.operation), str(self.op2)])

    def __repr__(self):
        return self.__str__()

    def __call__(self, js):
        """
        Return whether the JSON object passes the filter.
        """
        op1 = self.op1_getter(js)
        return self.operation(op1, self.op2)

    @classmethod
    def fromConfig(cls, config):
        """
        Create a filter from a dict with specifications.
        """
        op1_getter = config['op1']
        transform = config.get('transform')
        operation = config['operator']
        op2 = config['op2']

        return cls(op1_getter, operation, op2, transform)
