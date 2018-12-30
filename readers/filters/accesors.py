"""
Defines and facilitate access to a set of callables that will receive a row as input and will return a value
"""
import pyjq

def make_json_getter(getter_string):
    """
    Use jq-syntax to compile a query that will fetch the required value
    """
    try:
        getter = pyjq.compile(getter_string)
    except ValueError as err:
        raise ValueError(f'{getter_string} does not compile. {err}')
    return getter
