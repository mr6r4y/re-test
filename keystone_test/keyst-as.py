#!/usr/bin/env python3


import argparse
import keystone
import sys
import re
from hexdump import hexdump
import subprocess
from mako.template import Template
import tempfile
import os


def get_args():
    parser = argparse.ArgumentParser(description="Assemble a file using Keystone-engine")
    parser.add_argument("input_file", help="File to assemble")
    parser.add_argument("-o", "--output-file", help="Output into binary file")
    # parser.add_argument("-a", "--arch", help="Set architecture",
    #                     choices=["arm", "arm64", "mips", "x86", "ppc", "sparc", "systemz", "hexagon", "max"],
    #                     default="x86")
    # parser.add_argument("-m", "--mode", help="Set mode",
    #                     choices=["little_endian", "big_endian", "arm", "thumb", "v8", "micro", "mips3", "mips32r6",
    #                              "mips32", "mips64", "16", "32", "64", "ppc32", "ppc64", "qpx", "sparc32", "sparc64", "v9"],
    #                     default="64")

    return parser.parse_args()


class ElfGenerator(object):
    def __init__(self, code_encs, filename):
        l = len(code_encs)
        # self._compile_c_template(l, filename)
        self._compile_as_template(l, filename)
        self._patch_elf(filename, code_encs)

    @staticmethod
    def _compile_c_template(nop_count, filename):
        mako_tpl = """int _start()
{
% for i in range(nop_count):
    __asm__("nop");
% endfor
}
"""
        c_file = filename + ".keyst.c"
        open(c_file, "w").write(Template(mako_tpl).render(nop_count=nop_count))
        subprocess.Popen(["arm-linux-gnueabi-gcc", "-nostdlib", "-o", filename, c_file]).wait()
        os.unlink(c_file)

    @staticmethod
    def _compile_as_template(nop_count, filename):
        as_file = filename + ".keyst.asm"
        o_file = filename + ".keyst.o"

        mako_tpl = """.section .text
.global _start
_start:
% for i in range(nop_count):
nop
% endfor
"""
        open(as_file, "w").write(Template(mako_tpl).render(nop_count=nop_count))
        subprocess.Popen(["arm-linux-gnueabi-as", as_file, "-o", o_file]).wait()
        subprocess.Popen(["arm-linux-gnueabi-ld", "-N", o_file, "-o", filename]).wait()

        os.unlink(as_file)
        os.unlink(o_file)

    @staticmethod
    def _patch_elf(exec_file, code_encs):
        payload = "".join([("%02x" % i) for i in code_encs])

        r2_script = exec_file + "_patch.r2"
        open(r2_script, "w").write("s entry0; wx %s\n" % payload)
        subprocess.Popen(["r2", "-w", "-q", "-i", r2_script, exec_file]).wait()
        os.unlink(r2_script)


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
            ks = keystone.Ks(self._arch(arch), self._mode(mode))
            return ks.asm("\n".join(self.pcode))
        except keystone.KsError as e:
            print("ERROR: %s" % e)
            sys.exit(1)

    @staticmethod
    def make_elf(encs):
        pass


def main():
    args = get_args()

    code = open(args.input_file, "r").read()
    a = Assembler(code)

    print("Compiled code:")
    print("--------------")
    for i in a.pcode:
        print("    " + i)
    print("--------------")

    encs, count = a.asm("arm", "arm")

    print()
    print("Instruction count: %i" % count)
    print()
    print("Binary:\n")
    hexdump(bytes(encs))
    print()
    print("String Payload:\n\n%s" % repr(bytes(encs)))
    print()
    print()
    print("String Payload for r2:\n\n%s" % ("".join([("%02x" % i) for i in encs])))
    print()
    print()
    print("Generating ELF..")
    ElfGenerator(encs, args.input_file.split(".")[0] + ".keyst")
    print()
    print("Binary Size: %i" % len(encs))


if __name__ == '__main__':
    main()
