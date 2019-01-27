"""Basic text reader, reads any kind of text, either reading a line at a time or the whole file at once."""

class FileReader(object):
    """Read the file in `filename`

    :argument str filename: path to the file to be read.
    :argument str encoding: encoding.
    """
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.is_open = False
        self.file = None

    def open(self):
        """Open file if it is not already open
        
        :raises IOError: if the file is already open
        """
        if self.is_open:
            raise IOError('File already open: {}'.format(self.filename))
        self.file = open(self.filename, encoding=self.encoding)
        self.is_open = True
        return self.file

    def close(self):
        """Close file if it is open"""
        if self.is_open:
            self.file.close()
            self.file = None
            self.is_open = False

    def __enter__(self):
        """Open the file if it is not open and return :class:`self`"""
        if not self.is_open:
            self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the file and raise whatever exception was thrown with its message"""
        self.close()
        if exc_type:
            print(traceback)
            raise exc_type(exc_value)

    def read(self):
        """Reads the contents of the whole file.

        :returns: Contents of the file
        """
        if not self.is_open:
            self.open()
        return self.file.read()

    def __iter__(self):
        """ Allows iteration

        :returns: `self` to iter file
        """
        if not self.is_open:
            raise IOError('File not yet open. Use `open` method')
        return self

    def __next__(self):
        """
        :returns: next line of the file
        """
        return next(self.file)
