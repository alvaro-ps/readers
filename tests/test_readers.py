from unittest.mock import Mock, patch

from ..readers import FileReader, JSONReader

class TestFileReader():
    def test_whole_file():
        textfile = './test_files/test1.txt'

        print('Example reading a file')
        with FileReader(textfile) as filetext:
            print(filetext)

    def test_iter_file():
        with FileReader(textfile, iterable=True) as reader:
            for line in reader:
                print(line)

json_file = './test_files/test.json'
json_iterable_file = './test_files/test_iterable.json'


class TestJSONReader():
    def test_whole_file():
        print('Example reading a file')
        with JSONReader(json_file) as json_record:
            print(json_record.keys())

    def test_iter_file():
        print('Example iterating over a file')
        with JSONReader(json_iterable_file, iterable=True) as reader:
            for json_record in reader:
                print(json_record.keys())
