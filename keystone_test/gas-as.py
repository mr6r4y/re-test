#!/usr/bin/env python3


import argparse
import subprocess as sb
from hexdump import hexdump


def get_args():
    parser = argparse.ArgumentParser(description="Assemble a file using Keystone-engine")
    parser.add_argument("input_file", help="File to assemble")
    parser.add_argument("-o", "--output-file", help="Output into binary file")

    return parser.parse_args()


def assemble_as(asmcode):
    code = []
    for line in asmcode.split("\n"):
        l = line.split(";")[0].strip()
        # l = l.split("//")[0].strip()    # breaks one of the examples - has // in a string

        if l.startswith("#"):
            l = ""
        if l:
            code.append(l)

    fln = "/tmp/tmp-as.s"
    fln_o = "/tmp/tmp-as.o"
    fln_x = "/tmp/tmp-as.x"
    fln_b = "/tmp/tmp-as.b"
    open(fln, 'w').write(".section .text\n.global _start\n" + "\n".join(code))
    sb.Popen(["as", fln, "-o", fln_o]).wait()
    sb.Popen(["ld", "-N", fln_o, "-o", fln_x]).wait()
    sb.Popen(["objcopy", "-O", "binary", fln_x, fln_b]).wait()

    return open(fln_b, "rb").read()


def main():
    args = get_args()

    code = open(args.input_file, "r").read()
    rawbin = assemble_as(code)

    print()
    print("Binary:\n")
    hexdump(rawbin)
    print()
    print("String Payload:\n\n%s" % repr(rawbin))
    print()
    print("Binary Size: %i" % len(rawbin))

    if args.output_file:
        open(args.output_file, "w").write(rawbin)


if __name__ == '__main__':
    main()
