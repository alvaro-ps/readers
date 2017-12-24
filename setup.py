from distutils.core import setup

from readers import __version__

setup(
  name = 'readers',
  packages = ['readers'], # this must be the same as the name above
  version = __version__,
  description = 'Easy reading',
  author = 'apastors',
  author_email = 'a.pastor.sanchez@gmail.com',
  url = 'https://github.com/apastors/readers', # use the URL to the github repo
  download_url = 'https://github.com/apastors/readers/archive/{}.tar.gz'.format(__version__), # I'll explain this in a second
  keywords = ['reading', 'json', 'csv'], # arbitrary keywords
  classifiers = [],
)
