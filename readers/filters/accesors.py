"""
Defines and facilitate access to a set of callables that will receive a row as input and will return a value
"""
import pyjq

def get_value_from_json(js, getter_string):
    """
    Use jq-syntax to extract the desired value from the given json object
    """
    try:
        value = pyjq.first(getter_string, js)
    except ValueError as err:
        raise ValueError(f'{getter_string} does not compile. {err}')
    return value
