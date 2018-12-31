from pytest import raises

from readers.filters.value_getters import ValueGetter
from readers.filters.operations import identity

def test_compile_passes():
    getter_str = '.key[]'   

    getter = ValueGetter(getter_str)
    assert isinstance(getter, ValueGetter)
    assert getter.transform is identity

    transform = 'len'
    getter = ValueGetter(getter_str, transform=transform)
    assert isinstance(getter, ValueGetter)
    assert getter.transform is not identity

def test_compile_fails():
    getter_str = 'wrong jq query'

    with raises(ValueError) as err:
        getter = ValueGetter(getter_str)

def test_call_return_value():
    d = {'key': 1}
    getter_str = '.key'
    expected = 1

    getter = ValueGetter('.key')

    result = getter(d)
    assert result == expected

def test_call_return_list():
    d = {'key': [1, 2, 3]}
    getter_str = '.key'
    expected = [1, 2, 3]

    getter = ValueGetter('.key')

    result = getter(d)
    assert result == expected

def test__str__no_transform():
    getter_str = '.key'
    expected = '.key'

    getter = ValueGetter(getter_str)
    result = str(getter)
    assert result == expected

def test__str__transform():
    getter_str = '.key'
    transform = 'len'
    expected = '.key (transform: len)'

    getter = ValueGetter(getter_str, transform=transform)
    result = str(getter)
    assert result == expected
