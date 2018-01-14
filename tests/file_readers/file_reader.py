import os

import pytest

from readers import FileReader

textfile = os.sep + os.path.relpath('./tests/files/test1.txt', '/')
class TestFileReader(object):
    def test_init(self):
        f = FileReader(textfile)
        assert f.filename == textfile
        assert not f.iterable
        assert f.encoding == "utf-8"
        f.close()

    def test_enter(self):
        f = FileReader(textfile)
        result = f.__enter__()
        expected = "Hola, esta\nes una cadena\nde texto"
        assert result == expected
        f.close()

        f = FileReader(textfile, iterable=True)
        result = f.__enter__()
        expected = f
        assert result == expected
        f.close()

    def test_whole_fjile(self):
        expected = "Hola, esta\nes una cadena\nde texto"
        with FileReader(textfile) as filetext:
            assert filetext == expected

    def test_iter_file(self):
        expected = ["Hola, esta", "es una cadena", "de texto"]
        with FileReader(textfile, iterable=True) as reader:
            assert reader.encoding == "utf-8"
            assert reader.filename == textfile
            assert reader.iterable == True
            for line, expected_line in zip(reader, expected):
                assert line == expected_line

    def test_raises_exception(self):
        with pytest.raises(ValueError):
            with FileReader(textfile) as filetext:
                raise ValueError
