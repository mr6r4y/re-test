#!/usr/bin/env python3


from IPython.terminal.embed import InteractiveShellEmbed
from traitlets.config.loader import Config


from scapy.all import *


def main():
    a = 5
    b = 10

    c = Config()
    c.InteractiveShell.colors = 'Linux'
    c.InteractiveShell.confirm_exit = False
    c.TerminalIPythonApp.display_banner = False
    ipshell = InteractiveShellEmbed(config=c)
    ipshell()


if __name__ == '__main__':
    main()
