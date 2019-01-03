"""
- CSVReader:  reads CSV files, either one row per line or one list of namedtuples, one per row.
    It allows to specify delimiter and a list of fieldnames. See python's DictReader (https://docs.python.org/3/library/csv.html#csv.DictReader) for an explanation.
"""
import csv
from collections import namedtuple

from .file_reader import FileReader

class CSVReader(FileReader):
    """
    CSV files reader, allows to read a JSON file in two different ways:
        - Read the whole file at once and return it as a list of dicts.
        - Iterate over the file, returning one dict at a time.
    """
    def __init__(self, filename, delimiter=',', fieldnames=None, encoding='utf-8'):
        """Read the file in `filename`"""
        super().__init__(filename, encoding)
        self.fieldnames = fieldnames
        self.delimiter = delimiter

    def open(self):
        self.file = super().open()
        self.csvfile = csv.DictReader(self.file, fieldnames=self.fieldnames, delimiter=self.delimiter)
        return self.csvfile

    def read(self):
        if self.file is None:
            self.open()
        return [line for line in self.csvfile]

    def __next__(self):
        return next(self.csvfile)
