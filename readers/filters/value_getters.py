"""
Defines and facilitate access to a set of callables that will receive a row as input and will return a value
"""
import pyjq

from .operations import Operation

class ValueGetter(object):
    def __init__(self, getter_string, transform=None):
        """
        Use jq-syntax to compile a query that will fetch the required value
        """
        try:
            self.getter = pyjq.compile(getter_string)
        except ValueError as err:
            raise ValueError(f'{getter_string} does not compile. {err}')
        self.transform = Operation(transform) if transform is not None else lambda x: x

    def __call__(self, js):
        value = self.getter.apply(js)
        if len(value) == 1:
            value = value.pop()
        return self.transform(value)
