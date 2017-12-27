import os

from unittest.mock import Mock, patch

from readers import FileReader, JSONReader, CSVReader

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


json_file = os.sep + os.path.relpath('./tests/files/test.json', '/')
json_iterable_file = os.sep + os.path.relpath('./tests/files/test_iterable.json', '/')
class TestJSONReader(object):
    def test_whole_file(self):
        expected_keys = {"key1", "key2"}
        with JSONReader(json_file) as json_record:
            assert set(json_record.keys()) == expected_keys

    def test_iter_file(self):
        expected_values = list(range(1, 6))
        with JSONReader(json_iterable_file, iterable=True) as reader:
            for json_record, expected_value in zip(reader, expected_values):
                assert json_record['key2'] == expected_value


csv_file = os.sep + os.path.relpath('./tests/files/test.csv', '/')
class TestCSVReader(object):
    def test_whole_file(self):
        expected = [
            {"a": "1", "b": "2", "c": "3", "d": "4"},
            {"a": "5", "b": "6", "c": "7", "d": "8"},
            {"a": "9", "b": "10", "c": "11", "d": "12"},
        ]
        with CSVReader(csv_file) as csv_record:
            assert csv_record == expected

    def test_iter_file(self):
        expected = [
            {"a": "1", "b": "2", "c": "3", "d": "4"},
            {"a": "5", "b": "6", "c": "7", "d": "8"},
            {"a": "9", "b": "10", "c": "11", "d": "12"},
        ]
        with CSVReader(csv_file, iterable=True, header=True) as reader:
            for csv_record, expected_record in zip(reader, expected):
                assert csv_record == expected_record
