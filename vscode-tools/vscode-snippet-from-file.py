#!/usr/bin/env python3

import os
import sys
import argparse
import json


def get_args():
    parser = argparse.ArgumentParser(description="Turn a file into a .code-snippet")
    parser.add_argument("input_file", help="Path to file for turning it into a snippet")
    parser.add_argument("-n", "--snippet-name", default="snippet-name", help="Name and key of snippet")
    parser.add_argument("-s", "--scope", default="python", help="Set scope for snippet")

    args = parser.parse_args()
    return args


def process_line(line):
    return line.rstrip()


def main():
    args = get_args()
    if not os.path.isfile(args.input_file):
        print("Error: File %s does not exist!" % args.input_file, file=sys.stderr)
        sys.exit(1)

    with open(args.input_file, "r") as f:
        lines = list(map(process_line, f.readlines()))

    snippet = {
        args.snippet_name: {
            "scope": args.scope,
            "prefix": [args.snippet_name],
            "body": lines,
            "description": ""
        }
    }

    print(json.dumps(snippet, indent=4))


if __name__ == "__main__":
    main()