"""
- CSVReader:  reads CSV files, either one row per line or one list of namedtuples, one per row.
    It allows to specify delimiter and whether the file contains a header.
"""
import csv
from collections import namedtuple

from .file_reader import FileReader

class CSVReader(FileReader):
    """
    CSV files reader, allows to read a JSON file in two different ways:
        - Read the whole file at once and return it as a list of namedtuples.
        - Iterate over the file, returning one namedtuple at a time.
    """
    def __init__(self, filename, delimiter=',', header=False,
                 iterable=False, encoding='utf-8'):
        """
        Read the file in `filename`. If iterable=True, it can iterate over
        a file, returning one line at a time
        """
        FileReader.__init__(self, filename, iterable, encoding)
        self.header = header
        self.delimiter = delimiter

    def open_csv_file(self):
        self.open_file = open(self.filename, encoding=self.encoding)
        self.csvreader = csv.DictReader(self.open_file, delimiter=self.delimiter)
        return iter(self.csvreader)

    def __enter__(self):
        self.iter_csv_file = self.open_csv_file()

        if self.iterable:
            return self
        else:
            return self.read()

    def read(self):
        return [line for line in self]

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter_csv_file)
