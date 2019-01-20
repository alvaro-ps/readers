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

    def test__init__ok_transform1(self):
        op1 = '.a'
        transform='len'
        operator = 'ge'
        op2 = 4

        f = Filter(op1=op1, operator=operator, op2=op2, transform1=transform)
        assert isinstance(f, Filter)
        assert f.op1.transform is not identity
        assert str(f.op1.transform) == 'len'

    def test__init__ok_transform2(self):
        op1 = '.a'
        operator = 'ge'
        op2 = [1, 2, 3]
        transform='len'

        f = Filter(op1=op1, operator=operator, op2=op2, transform2=transform)
        assert isinstance(f, Filter)
        assert f.op2.transform is not identity
        assert str(f.op2.transform) == 'len'

    def test_fromConfig(self):
        config = {
            'op1': '.a',
            'transform1': 'len',
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

    def test__call__simple_ok_notransform(self):
        op1 = '.a'
        operator = 'ge'
        op2 = 3

        d = {'a': 5}
        expected = True

        f = Filter(op1=op1, operator=operator, op2=op2)
        assert f(d)

    def test__call__simple_ok_transform1(self):
        op1 = '.a'
        transform1 = 'len'
        operator = 'ge'
        op2 = 3

        d = {'a': [5, 6, 7, 8]}
        expected = True

        f = Filter(op1=op1, transform1=transform1, operator=operator, op2=op2)
        assert f(d) is expected

    def test__call__simple_ok_transform2(self):
        op1 = '.a'
        operator = 'le'
        op2 = [1, 2, 3, 4]
        transform2 = 'len'

        d = {'a': 3}
        expected = True

        f = Filter(op1=op1, operator=operator, op2=op2, transform2=transform2)
        assert f(d) is expected

    def test__call__simple_ok_transform_1and2(self):
        op1 = '.a'
        transform1 = 'len'
        operator = 'eq'
        op2 = [3, 4, 5, 6]
        transform2 = 'len'

        d = {'a': [1, 2, 3, 4]}
        expected = True

        f = Filter(op1=op1, transform1=transform1, operator=operator, op2=op2, transform2=transform2)
        assert f(d) is expected

    def test__call__simple_fail(self):
        op1 = '.a'
        operator = 'ge'
        op2 = {}

        d = {'a': 5}

        f = Filter(op1=op1, operator=operator, op2=op2)
        with raises(TypeError) as err:
            f(d)

    def test__call__complex_ok(self):
        config = {
            'operator': 'and',
            'op1': {
                'op1': '.a',
                'transform1': 'len',
                'operator': 'ge',
                'op2': 4
            },
            'op2': {
                'op1': '.a',
                'transform1': 'len',
                'operator': 'le',
                'op2': 5
            }
        }

        records = [
            {'a': [1, 2, 3, 4, 5]},
            {'a': [1, 2]}
        ]
        expected_results = [
            True,
            False
        ]

        f = Filter.fromConfig(config)
        for d, expected in zip(records, expected_results):
            assert f(d) == expected

    def test__call__complex_fail(self):
        config = {
            'operator': 'and',
            'op1': {
                'op1': '.a',
                'transform1': 'len',
                'operator': 'ge',
                'op2': 4
            },
            'op2': {
                'op1': '.a',
                'transform1': 'len',
                'operator': 'le',
                'op2': {}
            }
        }
        d = {'a': 5}

        f = Filter.fromConfig(config)
        with raises(TypeError) as err:
            f(d)
