try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Outlook for OS X Recent Address Parser',
    'author': 'Greg Lavallee',
    'url': 'https://github.com/elgreg/olk15RecentAddresses',
    'author_email': 'elgreg@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['RecentAddressesParser'],
    'scripts': [],
    'name': 'olk15RecentAddresses'
}

setup(**config)