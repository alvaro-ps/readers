import os

from pytest import raises

from readers import FileReader

textfile = os.sep + os.path.relpath('./tests/files/test1.txt', '/')
class TestFileReader(object):
    def test__init__(self):
        f = FileReader(textfile)
        assert f.filename == textfile
        assert f.encoding == "utf-8"
        assert not f.is_open
        assert f.file is None

    def test_open_closed_ok(self):
        f = FileReader(textfile)
        f.open()
        assert f.is_open
        f.close()
        assert not f.is_open

    def test_open_fails(self):
        f = FileReader('wrong file that does not exist')
        with raises(FileNotFoundError):
            f.open()

    def test__enter__(self):
        with FileReader(textfile) as reader:
            assert reader.is_open
        assert not reader.is_open

    def test_whole_file(self):
        expected = "Hola, esta\nes una cadena\nde texto\n"
        result = FileReader(textfile).read()
        assert result == expected

    def test_iter_file(self):
        expected = ["Hola, esta\n", "es una cadena\n", "de texto\n"]
        with FileReader(textfile) as reader:
            assert reader.encoding == "utf-8"
            assert reader.filename == textfile
            for line, expected_line in zip(reader, expected):
                assert line == expected_line
