"""JSONReader: reads JSON files, either one JSON per line or one JSON in the whole file"""
import json
from .file_reader import FileReader

class JSONReader(FileReader):
    """
    JSON files reader, allows to read a JSON file in two different ways:
        - Read the whole file at once and return it as a dict.
        - Iterate over the file, returning one dict at a time.
    """
    def read(self):
        return json.loads(super().read())

    def __next__(self):
        nextline = super().__next__()
        return json.loads(nextline)
