from readers.filters.value_getters import ValueGetter

def test_compile():
    getter_str = '.a'   
    expected = 5
    d = {'a': expected}

    getter = ValueGetter(getter_str)
    result = getter(d)
    assert result = expected
