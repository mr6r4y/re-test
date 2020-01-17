#!/usr/bin/env python3

from __future__ import unicode_literals

import os
import sys
import argparse

from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter, WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory


def get_args():
    parser = argparse.ArgumentParser(description="Test prompts")

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    session = PromptSession(history=FileHistory('/tmp/sctp-injector-inter.history'))
    SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
    script_file = session.prompt('Choose a Python sub-script to run inside > ',
            completer=PathCompleter(), validator=Validator.from_callable(lambda p: os.path.exists(p) and p.endswith(".py")),
            complete_while_typing=True)
    print('You said: %s' % script_file)


if __name__ == "__main__":
    main()