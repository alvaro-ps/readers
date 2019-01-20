from pytest import raises

from readers.filters.value_getters import ValueGetter
from readers.filters.operations import identity

class TestValueGetter():
    def test__init__notransfrom(self):
        getter_str = '.key[]'

        getter = ValueGetter(getter_str)
        assert isinstance(getter, ValueGetter)
        assert getter.transform is identity

    def test__init__transform(self):
        getter_str = '.key[]'
        transform = 'len'

        getter = ValueGetter(getter_str, transform=transform)
        assert isinstance(getter, ValueGetter)
        assert getter.transform is not identity

    def test__str__no_transform(self):
        getter_str = '.key'
        expected = '.key'

        getter = ValueGetter(getter_str)
        result = str(getter)
        assert result == expected

    def test__str__transform(self):
        getter_str = '.key'
        transform = 'len'
        expected = '.key (transform: len)'

        getter = ValueGetter(getter_str, transform=transform)
        result = str(getter)
        assert result == expected

    def test__repr__no_transform(self):
        getter_str = '.key'
        expected = '.key'

        getter = ValueGetter(getter_str)
        result = repr(getter)
        assert result == expected

    def test__repr__transform(self):
        getter_str = '.key'
        transform = 'len'
        expected = '.key (transform: len)'

        getter = ValueGetter(getter_str, transform=transform)
        result = repr(getter)
        assert result == expected

    def test__call__ok_return_value(self):
        d = {'key': 1}
        getter_str = '.key'
        expected = 1

        getter = ValueGetter(getter_str)

        result = getter(d)
        assert result == expected

    def test__call__ok_return_list(self):
        d = {'key': [1, 2, 3]}
        getter_str = '.key'
        expected = [1, 2, 3]

        getter = ValueGetter(getter_str)

        result = getter(d)
        assert result == expected

    def test__call__ok_return_constant_value(self):
        d = {}
        value = [1, 2, 3]
        expected = [1, 2, 3]

        getter = ValueGetter(value)

        result = getter(d)
        assert result == expected

    def test__call__fails(self):
        d = {'key': [1, 2, 3]}
        getter_str = '.wrong_key'

        getter = ValueGetter(getter_str)

        result = getter(d)
        assert result == None
