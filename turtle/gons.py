#!/usr/bin/env python3


from turtle import *


def main():
    # setx(-100)
    penup()
    setposition(0, -300)
    pendown()

    s = 10
    for i in range(3, 20):
        for j in range(i):
            forward(s)
            left(360/i)
        s += 10

    done()


if __name__ == '__main__':
    main()
