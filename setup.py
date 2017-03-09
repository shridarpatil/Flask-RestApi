from distutils.core import setup
setup(
  name = 'RestApi',
  packages = ['RestApi'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Create Rest Api',
  author = 'Shridhar Patil',
  author_email = 'shridharpatil2792@gmail.com',
  url = 'https://github.com/shridarpatil/Flask-RestApi', #URL to the github repo
  download_url = 'https://github.com/shridarpatil/Flask-RestApi/archive/0.0.1.tar.gz',
  keywords = ['RestApi', 'rest api', 'Rest Api'], # arbitrary keywords
  classifiers = [],
  install_requires=[
          'json', 'pymysql', 'flask',
      ],
)