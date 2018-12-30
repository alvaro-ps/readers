"""
Create a `Filter` object that needs to be compiled from an specification, and
that when called on an object, returns a boolean value.
"""
from .accesors import make_json_getter
from .operations import get_operation

class Filter(object):
    def __init__(self, op1_getter, operation, op2):
        """
        """
        self.op1_getter = make_json_getter(op1_getter)
        self.operation = get_operation(operation)
        self.op2 = op2
    def __call__(self, js):
        op1 = self.op1_getter.apply(js)
        return self.operation(op1, self.op2)
