#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import cracklib


class TestCaesar(unittest.TestCase):
    def test_bg_alphabet(self):
        self.assertNotEqual(cracklib.BG_ALPHABET.upper(), "")

    def test_bg_decrypt(self):
        cipher = "БЛП ЙТЛБУЖ ЕЖЧБУБ ГЙ ЕБ ВЬЕБУ ЙОУЖМЙДЖОУОЙ ШЖУЖУЖ ЙН РСЙЛБИЛЙ БЛП ЙТЛБУЖ ЕБ ТБ РП ЙОУЖМЙДЖОУОЙ ШЖУЖУЖ ЙН РПГЖШЖ РСЙЛБИЛЙ"
        key = 28
        msg = cracklib.rot_alphabet(cipher, key, cracklib.BG_ALPHABET.upper())

        self.assertNotEqual(msg, "")
        self.assertEqual(msg, "АКО ИСКАТЕ ДЕЦАТА ВИ ДА БЪДАТ ИНТЕЛИГЕНТНИ ЧЕТЕТЕ ИМ ПРИКАЗКИ АКО ИСКАТЕ ДА СА ПО ИНТЕЛИГЕНТНИ ЧЕТЕТЕ ИМ ПОВЕЧЕ ПРИКАЗКИ")


if __name__ == '__main__':
    unittest.main()
