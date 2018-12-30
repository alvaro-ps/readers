"""
Defines and facilitate access to a set of callables that will receive a row as input and will return a value
"""
import pyjq

class ValueGetter(object):
    def __init__(self, getter_string):
        """
        Use jq-syntax to compile a query that will fetch the required value
        """
        try:
            self.getter = pyjq.compile(getter_string)
        except ValueError as err:
            raise ValueError(f'{getter_string} does not compile. {err}')

    def __call__(self, js):
        value = self.getter.apply(js)
        if len(value) == 1:
            value = value.pop()
        return value
