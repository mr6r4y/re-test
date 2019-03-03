#!/usr/bin/env python3


import argparse
import keystone
import sys
import re
from hexdump import hexdump


def get_args():
    parser = argparse.ArgumentParser(description="Assemble a file using Keystone-engine")
    parser.add_argument("input_file", help="File to assemble")
    parser.add_argument("-o", "--output-file", help="Output into binary file")
    parser.add_argument("-a", "--arch", help="Set architecture",
                        choices=["arm", "arm64", "mips", "x86", "ppc", "sparc", "systemz", "hexagon", "max"],
                        default="x86")
    parser.add_argument("-m", "--mode", help="Set mode",
                        choices=["little_endian", "big_endian", "arm", "thumb", "v8", "micro", "mips3", "mips32r6",
                                 "mips32", "mips64", "16", "32", "64", "ppc32", "ppc64", "qpx", "sparc32", "sparc64", "v9"],
                        default="64")

    return parser.parse_args()


class Assembler(object):
    def __init__(self, code):
        self.code = self._normalize(code)
        self.pcode = [i for i in map(self._clean_comments, self.code) if i]
        self.arch = None
        self.mode = None

    @staticmethod
    def _normalize(code):
        return [i for i in map(lambda a: a.strip(), code.split("\n")) if i]

    @staticmethod
    def _clean_comments(line):
        l = line.split(";")[0].strip()
        # l = l.split("//")[0].strip()    # breaks one of the examples - has // in a string

        if l.startswith("#"):
            l = ""

        return l

    @staticmethod
    def _arch(arch_str):
        return keystone.__dict__["KS_ARCH_" + arch_str.upper()]

    @staticmethod
    def _mode(mode_str):
        return keystone.__dict__["KS_MODE_" + mode_str.upper()]

    def asm(self, arch, mode):
        try:
            # Initialize engine in X86-32bit mode
            ks = keystone.Ks(self._arch(arch), self._mode(mode))
            return ks.asm("\n".join(self.pcode))
        except keystone.KsError as e:
            print("ERROR: %s" % e)
            sys.exit(1)


def main():
    args = get_args()

    code = open(args.input_file, "r").read()
    a = Assembler(code)

    # print("Compiled code:")
    # print("--------------")
    # for i in a.pcode:
    #     print("    " + i)
    # print("--------------")

    encs, count = a.asm(args.arch, args.mode)

    print()
    print("Instruction count: %i" % count)
    print()
    print("Binary:\n")
    hexdump(bytes(encs))
    print()
    print("String Payload:\n\n%s" % repr(bytes(encs)))
    print()
    print("Binary Size: %i" % len(encs))


if __name__ == '__main__':
    main()
