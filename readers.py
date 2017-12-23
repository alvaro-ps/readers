"""Module with different readers
- AbstractReader: reads any kind of text, either reading a line at a time or the whole file at once.
- JSONReader: reads JSON files, either one JSON per line or one JSON in the whole file
"""

class AbstractReader(object):
    """
    """
    def __init__(self, filename, iterable=False, encoding='utf-8'):
        """
        """
        self.filename = filename
        self.iterable = iterable
        self.encoding = encoding

    def __enter__(self):
        self.open_file = open(self.filename, encoding=self.encoding)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

    def read(self):
        return "".join(line for line in open_file.readlines())
