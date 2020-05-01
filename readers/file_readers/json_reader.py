"""Reads JSON files, either one JSON per line or one JSON in the whole file"""
import json
from .file_reader import FileReader

class JSONReader(FileReader):
    """Read the JSON/NDJSON file in `filename`

    :argument str filename: path to the file to be read.
    :argument str encoding: encoding.
    """
    def read(self):
        """Reads the contents of the whole file.

        :returns: Contents of the JSON file as a :class:`dict`
        """
        return json.loads(super().read())

    def __next__(self):
        """
        :returns: next line of the file as a :class:`dict`
        """
        nextline = super().__next__()
        return json.loads(nextline)
