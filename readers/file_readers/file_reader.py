"""
- FileReader: reads any kind of text, either reading a line at a time or the whole file at once.
    Also gets rid of the EOL character (\n)
"""
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
            print(traceback)
            raise exc_type(exc_value)
        self.close_file()

    def read(self):
        return "".join(line for line in self.open_file)

    def __iter__(self):
        self.iter_open_file = iter(self.open_file)
        return self

    def __next__(self):
        return next(self.iter_open_file).strip()
