"""
- HTTPReader: extracts the HTML code from a url/list of urls, either reading
    returning a string with the text or an iterator yielding a string per url.
"""
import requests

class HTTPReader(object):
    """
    HTTPReader, allows to read a url/list of urls in two different ways:
        - Url: Scrapes the HTML in the url and return it as a string.
        - List of urls: scrapes all of them and return an iterator of strings.

    Use with the with statement.
    """
    def __init__(self, urls, encoding='utf-8'):
        """
        Scrape the content in urls. urls should be a string with a url
        or a list of urls.
        """
        self.urls = urls
        self.iterable = True if not isinstance(urls, str) else False
        self.encoding = encoding

    def fetch_html(self):
        self.html_file = open(self.filename, encoding=self.encoding)
        
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
        return "".join(line for line in self.open_file)

    def __iter__(self):
        self.iter_open_file = iter(self.open_file)
        return self

    def __next__(self):
        return next(self.iter_open_file).strip()
