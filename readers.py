"""Module with different readers
- AbstractReader: reads any kind of text, either reading a line at a time or the whole file at once.
    Also gets rid of the EOL character (\n)
- JSONReader: reads JSON files, either one JSON per line or one JSON in the whole file
"""

class AbstractReader(object):
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
        self.open_file()
        if self.iterable:
            return self
        else:
            return self.open_file.read()

    def __exit__(self, *args):
        self.close_file()

    def read(self):
        return "".join(line for line in open_file.readlines())

    def __iter__(self):
        self.iter_open_file = iter(self.open_file)
        return self

    def __next__(self):
        return next(self.iter_open_file).strip()
