from setuptools import setup
import sys


if sys.version_info < (3,6,7):
    sys.exit('Sorry, Python 3.6.7+ is supported only')

setup(
    name = 'dload',
    version = '0.1.0',
    packages = ['dload'],
    description = "Python command line application to download files using several protocols",
    author = "Shehabul Hossain",
    author_email = "hello@shehabul.com",
    python_requires='>=3.6.7',
    url = "https://shehabul.com",
    install_requires=[
        'paramiko'
    ],
    entry_points = {
        'console_scripts': [
            'dload = dload.main:main'
        ]
    })