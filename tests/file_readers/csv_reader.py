import os

from readers.file_readers import CSVReader

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
