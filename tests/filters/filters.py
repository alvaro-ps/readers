from pytest import raises

from readers.filters.filters import Filter
from readers.filters.operations import identity

class TestFilter():
    def test__init__ok_notransform(self):
        op1 = '.a'
        operator = 'ge'
        op2 = 4

        f = Filter(op1=op1, operator=operator, op2=op2)
        assert isinstance(f, Filter)
        assert f.op1.transform is identity

    def test__init__ok_transform(self):
        op1 = '.a'
        transform='len'
        operator = 'ge'
        op2 = 4

        f = Filter(op1=op1, operator=operator, op2=op2, transform=transform)
        assert isinstance(f, Filter)
        assert f.op1.transform is not identity
        assert str(f.op1.transform) == 'len'

    def test__init__fail(self):
        op1 = 'a'
        operator = 'ge'
        op2 = 3

        with raises(TypeError) as err:
            f = Filter(op1=op1, operator=operator, op2=op2)

    def test_fromConfig(self):
        config = {
            'op1': '.a',
            'transform': 'len',
            'operator': 'ge',
            'op2': 4
        }
        f = Filter.fromConfig(config)
        assert isinstance(f, Filter)
        assert f.op1.transform is not identity
        assert str(f.op1.transform) == 'len'

    def test__str__(self):
        op1 = '.a'
        operator = 'ge'
        op2 = 3
        f = Filter(operator, op1, op2)
        expected = '(.a - ge - 3)'
        assert str(f) == expected

    def test__repr__(self):
        op1 = '.a'
        operator = 'ge'
        op2 = 3
        f = Filter(operator, op1, op2)
        expected = '(.a - ge - 3)'
        assert repr(f) == expected

    def test__call__ok(self):
        op1 = '.a'
        operator = 'ge'
        op2 = 3

        d = {'a': 5}
        expected = True

        f = Filter(op1=op1, operator=operator, op2=op2)
        assert f(d)

    def test__call__fail(self):
        op1 = '.a'
        operator = 'ge'
        op2 = {}

        d = {'a': 5}

        f = Filter(op1=op1, operator=operator, op2=op2)
        with raises(TypeError) as err:
            f(d)
