"""Module with different readers
- FileReader: reads any kind of text, either reading a line at a time or the whole file at once.
    Also gets rid of the EOL character (\n)
- JSONReader: reads JSON files, either one JSON per line or one JSON in the whole file
"""
import json

class FileReader(object):
    """
    Reader, allows to read a file in two different ways:
        - Read the whole file at once and return it as a string.
        - Iterate over the file, one line at a time.

    Use with the with statement.
    """
    def __init__(self, filename, iterable=False, encoding='utf-8'):
        """
        Read the file in `filename`. If iterable=True, it can iterate over
        a file, returning one line at a time
        """
        self.filename = filename
        self.iterable = iterable
        self.encoding = encoding

    def open_file(self):
        self.open_file = open(self.filename, encoding=self.encoding)
        
    def close_file(self):
        self.open_file.close()

    def __enter__(self):
        """
        whatever is returned here is set to the variable
        after the 'as' in the 'with' statement.
        If iterable, return the whole object, which can be
            iterated.
        if not, return the read text
        """
        self.open_file()
        if self.iterable:
            return self
        else:
            return self.open_file.read()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(exc_type)
            print(exc_value)
            print(exc_traceback)
        self.close_file()

    def read(self):
        return "".join(line for line in open_file.readlines())

    def __iter__(self):
        self.iter_open_file = iter(self.open_file)
        return self

    def __next__(self):
        return next(self.iter_open_file).strip()

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
