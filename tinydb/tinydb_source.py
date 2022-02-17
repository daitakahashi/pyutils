#!/usr/bin/env python3

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

import tinydb


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument(
        'input', type=Path, nargs='?', default='-',
        help='input DB (default: "-" read from stdin)'
    )
    parser.add_argument(
        'output', type=Path, nargs='?', default='-',
        help='output JSON array (default: "-" dump to stdout)'
    )
    parser.add_argument(
        '--append', action='store_true',
        help='append data to existing contents'
    )
    args = parser.parse_args(argv)
    return args


def main(argv):
    args = parse_args(argv[1:])
    if str(args.input) == '-':
        input_data = json.load(sys.stdin)
        db = tinydb.TinyDB(storage=tinydb.storages.MemoryStorage)
        db.storage.write(input_data)
    else:
        db = tinydb.TinyDB(args.input, access_mode='r')
    if str(args.output) == '-':
        print(json.dumps(db.all()))
    else:
        with args.output.open(encoding='utf-8') as outfile:
            json.dump(db.all(), outfile)


if __name__ == '__main__':
    main(sys.argv)
