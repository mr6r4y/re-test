#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import logging
import sys
from Crypto.Util.number import inverse
from cracklib import modinv


class TestMisc(unittest.TestCase):
    def test_inverse_1(self):
        a, b = 32, 59
        self.assertEqual(modinv(a, b), inverse(a, b))

    def test_inverse_2(self):
        a, b = 322, 534
        # self.assertEqual(modinv(a, b), inverse(a, b))
        logging.info("modinv(..)=%s, inverse(..)=%i" % (modinv(a, b), inverse(a, b)))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(levelname)s:%(funcName)s:  %(message)s")
    unittest.main()
