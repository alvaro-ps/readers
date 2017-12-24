import os

from unittest.mock import Mock, patch

from readers import FileReader, JSONReader

textfile = os.sep + os.path.relpath('./tests/files/test1.txt', '/')
class TestFileReader():
    def test_whole_file(self):
        with FileReader(textfile) as filetext:
            assert filetext

    def test_iter_file(self):
        with FileReader(textfile, iterable=True) as reader:
            for line in reader:
                assert line


json_file = os.sep + os.path.relpath('./tests/files/test.json', '/')
json_iterable_file = os.sep + os.path.relpath('./tests/files/test_iterable.json', '/')
class TestJSONReader():
    def test_whole_file(self):
        with JSONReader(json_file) as json_record:
            assert json_record.keys()

    def test_iter_file(self):
        with JSONReader(json_iterable_file, iterable=True) as reader:
            for json_record in reader:
                assert json_record.keys()
