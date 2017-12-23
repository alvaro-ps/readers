"""
- CSVReader:  reads CSV files, either one row per line or one list of namedtuples, one per row.
    It allows to specify delimiter and whether the file contains a header.
"""
import csv
from collections import namedtuple

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

    def __enter__(self):
        reader = FileReader.__enter__(self)
        csvreader = csv.reader(reader, delimiter=self.delimiter)
        if self.header:
            header = next(csvreader)
            self.row = namedtuple('row', header)

        if self.iterable:
            return csvreader
        else:
            return self.read()

    def read(self):
        return FileReader.read(self)

    def __iter__(self):
        return FileReader.__iter__(self)

    def __next__(self):
        return self.row(FileReader.__next__(self).split(self.delimiter))
