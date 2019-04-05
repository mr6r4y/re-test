#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import sys
import unittest
import string
import cracklib


ALPHABET = string.ascii_uppercase
MSG = "If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell"
CIPHER = "Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"
KEY = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'


class TestSimpleSub(unittest.TestCase):
    def test_encrypt(self):
        a = cracklib.SimpleSubstitutionCipher(ALPHABET)
        cipher = a.encrypt(MSG.upper(), KEY)

        logging.info("CIPHER: %s" % cipher)
        self.assertEqual(CIPHER.upper(), cipher)

    def test_decrypt(self):
        a = cracklib.SimpleSubstitutionCipher(ALPHABET)
        msg = a.decrypt(CIPHER.upper(), KEY)

        logging.info("MSG: %s" % msg)
        self.assertEqual(MSG.upper(), msg)

    def test_random_key(self):
        a = cracklib.SimpleSubstitutionCipher(ALPHABET)
        k1 = a.random_key()
        k2 = a.random_key()

        logging.info("key-1: %s" % k1)
        logging.info("key-2: %s" % k2)
        self.assertNotEqual(k1, k2)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(levelname)s:%(funcName)s:  %(message)s")
    unittest.main()
