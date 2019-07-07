#!/usr/bin/env python3.6


from tabulate import tabulate


def main():
    l = [["0x%X" % i for i in range(0x11)]]
    for i in range(0x11):
        l.append(["0x%X" % i]+["0x%X" % (j*i) for j in range(0x11)])

    print(tabulate(l, tablefmt='rst',  headers="firstrow"))


if __name__ == '__main__':
    main()
