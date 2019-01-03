"""FileReader: reads any kind of text, either reading a line at a time or the whole file at once."""

class FileReader(object):
    """Basic text reader."""
    def __init__(self, filename, encoding='utf-8'):
        """Read the file in `filename`"""
        self.filename = filename
        self.encoding = encoding
        self.is_open = False
        self.file = None

    def open(self):
        if self.file is not None:
            raise IOError('File already open: {}'.format(self.filename))
        self.file = open(self.filename, encoding=self.encoding)
        self.is_open = True
        return self.file

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
            self.is_open = False

    def __enter__(self):
        """Open the file if it is not open and return"""
        if self.file is None:
            self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        if exc_type:
            print(traceback)
            raise exc_type(exc_value)

    def read(self):
        if self.file is None:
            self.open()
        return self.file.read()

    def __iter__(self):
        if self.file is None:
            raise IOError('File not yet open. Use `open` method')
        return self

    def __next__(self):
        return next(self.file)
