"""
- JSONReader: reads JSON files, either one JSON per line or one JSON in the whole file
"""
import json

class JSONReader(FileReader):
    """
    JSON files reader, allows to read a JSON file in two different ways:
        - Read the whole file at once and return it as a dict.
        - Iterate over the file, returning one dict at a time.
    """
    def __init__(self, filename, iterable=False, encoding='utf-8'):
        """
        Read the file in `filename`. If iterable=True, it can iterate over
        a file, returning one line at a time
        """
        FileReader.__init__(self, filename, iterable, encoding)

    def __enter__(self):
        reader = FileReader.__enter__(self)
        if self.iterable:
            return reader
        else:
            return json.loads(reader)

    def read(self):
        return json.loads(FileReader.read(self))

    def __iter__(self):
        return FileReader.__iter__(self)

    def __next__(self):
        return json.loads(FileReader.__next__(self))
