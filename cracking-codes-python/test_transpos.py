#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import cracklib


class TestTranspos(unittest.TestCase):
    def test_encrypt(self):
        msg = "Common sense is not so common."
        key = 8

        cipher = cracklib.enc_transpos(msg, key)

        self.assertEqual(cipher, "Cenoonommstmme oo snnio. s s c")

    def test_decrypt(self):
        cipher = "Cenoonommstmme oo snnio. s s c"
        key = 8

        msg = cracklib.dec_transpos(cipher, key)

        self.assertEqual(msg, "Common sense is not so common.")


if __name__ == '__main__':
    unittest.main()
