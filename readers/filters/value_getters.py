"""
Defines and facilitate access to a set of callables that will receive a row as input and will return a value
"""
import pyjq

from .operations import Operation, identity

class ValueGetter(object):
    def __init__(self, value, transform=None):
        """
        Creates a value getter that will return a value when applied on a JSON object.
        `value` can be :
            - jq-like string that will fetch the required value from the JSON object.
            - a constant value that will be returned regardless of the JSON object.

        If transform is specified, it will be applied to the value before it is returned
        """
        self.value = value
        try:
            self.getter = pyjq.compile(value)
        except (AttributeError, ValueError) as err:
            self.getter = None
        self.transform = Operation(transform) if transform is not None else identity

    def __str__(self):
        string = str(self.value)
        if self.transform is not identity:
            string = string + " (transform: {transform})".format(transform=self.transform)
        return string

    def __repr__(self):
        return self.__str__()

    def __call__(self, js):
        if self.getter:
            try:
                value = self.getter.one(js)
            except IndexError:
                value = self.getter.all(js)
        else:
            value = self.value
        return self.transform(value)
