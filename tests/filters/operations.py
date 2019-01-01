from pytest import raises

from readers.filters.operations import Operation, OPERATORS

def test_identity():
    f = OPERATORS['identity']

    x = 'a'
    expected = x
    result = f(x)
    assert result == expected

def test_toset():
    f = OPERATORS['to_set']

    x = 'a'
    expected = {'a'}
    result = f(x)
    assert result == expected

def test_issubset():
    f = OPERATORS['issubset']

    x = {1, 2}
    y = {1, 2, 3}
    expected = True
    result = f(x, y)
    assert result == expected

    x = {1, 2, 3}
    y = {1, 2}
    expected = False
    result = f(x, y)
    assert result == expected

def test_issuperset():
    f = OPERATORS['issuperset']

    x = {1, 2}
    y = {1, 2, 3}
    expected = False
    result = f(x, y)
    assert result == expected

    x = {1, 2, 3}
    y = {1, 2}
    expected = True
    result = f(x, y)
    assert result == expected

def test_intersects():
    f = OPERATORS['intersects']

    x = {1, 2}
    y = {1, 2, 3}
    expected = True
    result = f(x, y)
    assert result == expected

    x = {1, 2, 3}
    y = {4, 5}
    expected = False
    result = f(x, y)
    assert result == expected

def test_nintersects():
    f = OPERATORS['nintersects']

    x = {1, 2}
    y = {1, 2, 3}
    expected = False
    result = f(x, y)
    assert result == expected

    x = {1, 2, 3}
    y = {4, 5}
    expected = True
    result = f(x, y)
    assert result == expected

def test_in():
    f = OPERATORS['in']

    x = 1
    y = {1, 2, 3}
    expected = True
    result = f(x, y)
    assert result == expected

    x = 1
    y = {4, 5}
    expected = False
    result = f(x, y)
    assert result == expected

def test_nin():
    f = OPERATORS['nin']

    x = 1
    y = {1, 2, 3}
    expected = False
    result = f(x, y)
    assert result == expected

    x = 1
    y = {4, 5}
    expected = True
    result = f(x, y)
    assert result == expected

class TestOperation():
    def test__init__ok(self):
        name = 'len'
        op = Operation(name)

        assert isinstance(op, Operation)

    def test__init__fail(self):
        name = 'wrong operator'
        with raises(KeyError) as err:
            op = Operation(name)

    def test__call__ok(self):
        name = 'to_set'
        op1 = 1

        expected = {1}
        op = Operation(name)
        result = op(op1)

        assert expected == result

    def test__str__(self):
        name = 'len'
        op = Operation(name)
        assert str(op) == name

    def test__repr__(self):
        name = 'len'
        op = Operation(name)
        assert repr(op) == name
