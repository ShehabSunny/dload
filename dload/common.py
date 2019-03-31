import argparse
import os
import sys
from urllib.parse import urlparse


class WritableDir(argparse.Action):
    """
    check if provided directory is valid and writable
    """
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            print(f"{prospective_dir} is not a valid path")
            sys.exit(1)
        if os.access(prospective_dir, os.W_OK):
            setattr(namespace,self.dest,prospective_dir)
        else:
            print(f"{prospective_dir} is not a writable dir")
            sys.exit(1)


def parse_protocol(url="") -> str:
    o = urlparse(url)
    return o.scheme

def parse_host(url="") -> str:
    o = urlparse(url)
    return o.hostname

def parse_port(url="") -> str:
    o = urlparse(url)
    return o.port
