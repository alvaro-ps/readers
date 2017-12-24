import os

from unittest.mock import Mock, patch

from readers import FileReader, JSONReader

textfile = os.sep + os.path.relpath('./tests/files/test1.txt', '/')
class TestFileReader():
    def test_whole_fjile(self):
        expected = "Hola, esta\nes una cadena\nde texto\n"
        with FileReader(textfile) as filetext:
            assert filetext == expected

    def test_iter_file(self):
        expected = ["Hola, esta", "es una cadena", "de texto"]
        with FileReader(textfile, iterable=True) as reader:
            for line, expected_line in zip(reader, expected):
                assert line == expected_line


json_file = os.sep + os.path.relpath('./tests/files/test.json', '/')
json_iterable_file = os.sep + os.path.relpath('./tests/files/test_iterable.json', '/')
class TestJSONReader():
    def test_whole_file(self):
        expected_keys = {"key1", "key2"}
        with JSONReader(json_file) as json_record:
            assert set(json_record.keys()) == expected_keys

    def test_iter_file(self):
        with JSONReader(json_iterable_file, iterable=True) as reader:
            for json_record in reader:
                assert json_record.keys()
