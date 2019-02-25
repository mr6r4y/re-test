#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import sys
import unittest
import cracklib
import string


ALPHABET = string.ascii_letters + string.digits
MSG = "A computer would deserve to be called intelligent if it could deceive a human into believing that it was human."
CIPHER = "W ayu5Kde9 OyKXH HeGe9he dy De a6XXeH m1deXXmie1d mL md ayKXH Heaemhe 6 PKu61 m1dy DeXmehm1i dP6d md O6G PKu61."
KEY = 2104


class TestAffine(unittest.TestCase):
    def test_generate_key(self):
        a = cracklib.Affine(ALPHABET)
        k = a.generate_key()

        k1, k2 = a._split_key(k)
        self.assertTrue(cracklib.gcd(k1, a.alphabet_len) == 1)

    def test_encrypt(self):
        a = cracklib.Affine(ALPHABET)
        cipher = a.encrypt(MSG, KEY)

        self.assertEqual(CIPHER, cipher)

    def test_decrypt(self):
        a = cracklib.Affine(ALPHABET)
        msg = a.decrypt(CIPHER, KEY)

        self.assertEqual(MSG, msg)

    def test_cracking(self):
        a = cracklib.Affine(ALPHABET)
        keys = cracklib.crack_affine(CIPHER, ALPHABET)

        self.assertTrue(isinstance(keys, list) and len(keys) > 0, "The key is not generated")

        for k in keys:
            logging.info("key={:d}".format(k))
            logging.info("msg='{:s}'".format(a.decrypt(CIPHER, k)))

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    unittest.main()
