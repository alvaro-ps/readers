"""Reads CSV files, either one row per line or one list of :class:`dict`, one per row.
It allows to specify delimiter and a list of fieldnames. See python's :class:`csv.DictReader` for an explanation.
"""
import csv
from collections import namedtuple

from .file_reader import FileReader

class CSVReader(FileReader):
    """Read the CSV file in `filename`

    :argument str filename: path to the file to be read.
    :argument str encoding: encoding.
    """
    def __init__(self, filename, delimiter=',', fieldnames=None, encoding='utf-8'):
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
