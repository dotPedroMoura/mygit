import argparse
import os

from . import data
from .data import GIT_DIRECTORY


def main():
    args = parse_arguments()
    args.function(args)

def parse_arguments():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest = 'command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(function = init)

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(function = hash_object)
    hash_object_parser.add_argument('file')

    return parser.parse_args()

def init(args):
    data.init()
    print(f'Initialized empty mygit repository in {os.path.join(os.getcwd(), GIT_DIRECTORY)}')

def hash_object(args):
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))