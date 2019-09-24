#!/usr/bin/env python3

def byte_rev(x):
    x = (x & 0x55) << 1 | (x & 0xAA) >> 1
    x = (x & 0x33) << 2 | (x & 0xCC) >> 2
    x = (x & 0x0F) << 4 | (x & 0xF0) >> 4

    return x


def bin(x):
    return "{0:08b}".format(x)


def main():
    xx = 0x32
    print(hex(xx))
    print(bin(xx))
    y = byte_rev(xx)
    print(hex(y))
    print(bin(y))


if __name__ == "__main__":
    main()
