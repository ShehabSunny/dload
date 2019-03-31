from .common import WritableDir
from .client import Client

import argparse
import sys
import os


def main():
    """
    Entry point of the application.
    """
    try:
        args = init_cli()
        print("Starting the application..")
        print(f"Download path: {args.location} \n")
        download_location = args.location
        client = Client(download_location)
        if args.file is not None:
            for line in args.file:
                client.download(line.rstrip())

        if args.urls is not None:   
            for url in args.urls:
                client.download(url.rstrip())
    except KeyboardInterrupt:
        # remove all temp files
        sys.exit(0)


def init_cli():
    """
    initialize the CLI application. 
    Add, validate, and parse all the arguments required to run this application.
    """
    # initialize the parser
    parser = argparse.ArgumentParser(
        description='Download a file from URL.',
        formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=52)
    )
    group = parser.add_mutually_exclusive_group()

    # ==================================================
    # add argument for URLS
    # ==================================================
    group.add_argument(
        '-u',
        '--urls', 
        help='URLs to be downloaded from',
        nargs='+',
        type=str
    )

    # ==================================================
    # add optional argument for file input
    # ==================================================
    group.add_argument(
        '-f',
        '--file',
        help='specify an alternative file with all the urls separated by new line',
        nargs='?',
        type=argparse.FileType('r', encoding='utf-8'),
    )

    # ==================================================
    # add optional argument for download location folder
    # ==================================================

    # create default download path if does not exist
    d_location = os.path.join(os.path.expanduser('~'), 'data')
    yes, msg = create_check_writable_dir(d_location)
    if not yes:
        print(msg)
        print("\nPlease create and/or update permission for the directory \
            or provide a download location with -f/--file")
        sys.exit(1)

    # add argument
    parser.add_argument(
        '-l',
        '--location',
        help='specify a download location (default is $HOME/data)',
        nargs='?',
        default=d_location,
        action=WritableDir
    )
    
    # parse arguments
    args = parser.parse_args()
    return args    


def create_check_writable_dir(d_location):
    try:
        os.makedirs(d_location, exist_ok=True)
    except OSError as e:
        return False, f"could not create directory: {str(e)}"
    if os.access(d_location, os.W_OK):
        return True, ""
    else:
        return False, f"no write access for directory: {d_location}"

    
