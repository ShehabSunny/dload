from setuptools import setup

setup(
    name = 'dload',
    version = '0.1.0',
    packages = ['dload'],
    description = "Python command line application to download files using several protocols",
    author = "Shehabul Hossain",
    author_email = "hello@shehabul.com",
    python_requires='>=3.7.0',
    url = "https://shehabul.com",
    install_requires=[
        'paramiko'
    ],
    entry_points = {
        'console_scripts': [
            'dload = dload.main:main'
        ]
    })