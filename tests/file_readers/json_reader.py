import os

from readers.file_readers import JSONReader

json_file = os.sep + os.path.relpath('./tests/files/test.json', '/')
json_iterable_file = os.sep + os.path.relpath('./tests/files/test_iterable.json', '/')
class TestJSONReader(object):
    def test_whole_file(self):
        expected_keys = {"key1", "key2"}
        json_record = JSONReader(json_file).read()
        assert set(json_record.keys()) == expected_keys

    def test_iter_file(self):
        expected_values = list(range(1, 6))
        with JSONReader(json_iterable_file) as reader:
            for json_record, expected_value in zip(reader, expected_values):
                assert json_record['key2'] == expected_value
