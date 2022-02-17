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
        help='input JSON array (default: "-" read from stdin)'
    )
    parser.add_argument(
        'output', type=Path, nargs='?', default='-',
        help='output DB (default: "-" dump to stdout)'
    )
    parser.add_argument(
        '--append', action='store_true',
        help='append data to existing contents'
    )
    args = parser.parse_args(argv)
    return args


def main(argv):
    args = parse_args(argv[1:])
    if str(args.output) == '-':
        dump_to_stdout = True
        db = tinydb.TinyDB(storage=tinydb.storages.MemoryStorage)
    else:
        dump_to_stdout = False
        if args.output.exists() and not args.append:
            args.output.unlink()
        db = tinydb.TinyDB(args.output)
    with db as output_db:
        if str(args.input) == '-':
            input_data = json.load(sys.stdin)
        else:
            with args.input.open(encoding='utf-8') as infile:
                input_data = json.load(infile)
        output_db.insert_multiple(input_data)
        if dump_to_stdout:
            print(json.dumps(db.storage.read()))


if __name__ == '__main__':
    main(sys.argv)
