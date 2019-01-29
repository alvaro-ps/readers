"""Defines a getter that, when calling a JSON object, returns a value. This definition can be:

* a **jq-like expression**:  ``'.key1[].key2'``
* a **value**: anything that does not compile to a jq query ``(1, [1, 2, 3], 'string')``

Optionally, a transform operation can be applied after the value is extracted. This operation must
accept **one** parameter:

* `len` when the getter returns a list
* `int` in order to convert a string to a numeric value, ...

See :mod:`readers.filters.operations`.

Usage
-----
.. code-block:: python

    >>> from readers.filters.value_getters import ValueGetter
    >>> js = {
    ...     "key1": [
    ...         {"key2": 1},
    ...         {"key2": 2},
    ...         {"key2": 3}
    ...     ]
    ... }
    >>> g = ValueGetter('.key1[].key2')
    >>> g(js)
    [1, 2, 3]
    >>> g = ValueGetter('.key1[].key2', transform='len')
    >>> g(js)
    3
    >>> g = ValueGetter(5)
    >>> g(js)
    5
"""
import pyjq

from .operations import Operation, identity

class ValueGetter(object):
    """Creates a value getter that will return a value when applied on a JSON object.
    
    :argument value:

        * a **jq-like expression**:  ``'.key1[].key2'``
        * a **value**: anything that does not compile to a jq query (``1``, ``[1, 2, 3]``, ``'string'``)

    :argument transform: operation name that will be passed on to :class:`Operation <readers.filters.operations.Operation>`
    """
    def __init__(self, value, transform=None):
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
        """Call the getter on the passed json object and return the value (transformed if required)

        :argument ``js``: JSON :class:`dict`.
        :returns: [transformed] value from ``js``
        """
        if self.getter:
            value = self.getter.apply(js)
        else:
            value = self.value
        return self.transform(value)
