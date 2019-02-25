# -*- coding: utf-8 -*-
"""Cryptography utility library

Collection of crypto functions while working on Cracking Codes with Python.
"""

import string
import math
import random
from functools import reduce
import enchant


BG_ALPHABET = "абвгдежзийклмнопрстуфцчшщъьюя"
EN_ALPHABET = string.ascii_lowercase


def rot_alphabet(msg, key, alphabet):
    """Rotate(Caesar) encryption over given alphabet

    The key difference between other `rot` implementations
    is the alphabet that is given and used for this operation.

    Args:
        msg (str): Message to encrypt/decrypt
        key (int): Key used for letter shifting
        alphabet (str): The alphabet to rotate/shift upon

    Returns:
        str: Encrypted/decrypted message
    """

    ns = []
    for i in msg:
        ns.append(alphabet[(alphabet.index(i) + key) % len(alphabet)] if i in alphabet else i)

    return "".join(ns)


def enc_transpos(msg, key):
    """Encrypt using transposition cipher

    Taken from http://inventwithpython.com/cracking/chapter7.html

    Args:
        msg (str): Message to encrypt
        key (int): Key which is a simple number

    Returns:
        str: Cipher text
    """

    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        current_index = column

        # Keep looping until current_index goes past the message length:
        while current_index < len(msg):
            # Place the character at current_index in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += msg[current_index]

            # Move current_index over:
            current_index += key

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)


def dec_transpos(cipher, key):
    """Decrypt using transposition cipher

    Taken from http://inventwithpython.com/cracking/chapter8.html

    Args:
        cipher (str): Cipher text
        key (int): Decryption key

    Returns:
        str: Plain text message
    """

    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    columns_number = int(math.ceil(len(cipher) / float(key)))
    # The number of "rows" in our grid:
    rows_number = key
    # The number of "shaded boxes" in the last "column" of the grid:
    shaded_boxes_number = (columns_number * rows_number) - len(cipher)

    # Each string in plaintext represents a column in the grid:
    plaintext = [''] * columns_number

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in cipher:
        plaintext[column] += symbol
        column += 1 # Point to the next column.

        # If there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row:
        if (column == columns_number) or \
           (column == columns_number - 1 and row >= rows_number - shaded_boxes_number):
            column = 0
            row += 1

    return ''.join(plaintext)


def gcd(a, b):
    """Greatest Common Divisor

    Find the GCD of `a` and `b`

    Args:
        a (int)
        b (int)

    Returns:
        int
    """

    while a != 0:
        a, b = b % a, a
    return b


def modinv(a, m):
    """Search for modular inverse of `a` and `m`

    Uses Extended Euclidean algorithm.

    Args:
        a (int)
        m (int)

    Returns:
        int
    """

    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m = 1.

    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.

    # Calculate using the extended Euclidean algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


class AffineError(Exception):
    pass


class Affine(object):
    """Affine cipher class

    Handles encryption, decryption and key generation.
    """

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.alphabet_len = len(alphabet)

    def _split_key(self, key):
        k1, k2 = key // self.alphabet_len, key % self.alphabet_len

        return k1, k2

    def check_key(self, key):
        k1, k2 = self._split_key(key)
        return (gcd(k1, self.alphabet_len) == 1) and (k1 != 1) and (k2 != 0)

    def generate_key(self):
        while True:
            k1, k2 = random.randint(2, self.alphabet_len), random.randint(2, self.alphabet_len)
            key = k1 * self.alphabet_len + k2
            if self.check_key(key):
                return key

    def encrypt(self, msg, key):
        if not self.check_key(key):
            raise AffineError("Weak key")

        k1, k2 = self._split_key(key)
        cipher = []

        for c in msg:
            if c in self.alphabet:
                i = self.alphabet.find(c)
                c = self.alphabet[(i * k1 + k2) % self.alphabet_len]
            cipher.append(c)

        return "".join(cipher)

    def decrypt(self, cipher, key):
        if not self.check_key(key):
            raise AffineError("Weak key")

        k1, k2 = self._split_key(key)
        k1_inverse = search_modinv(k1, self.alphabet_len)

        msg = []

        for c in cipher:
            if c in self.alphabet:
                i = self.alphabet.find(c)
                c = self.alphabet[(i - k2) * k1_inverse % self.alphabet_len]
            msg.append(c)

        return "".join(msg)


def is_speach(sentence, lang="en_US"):
    def _truth_ratio(a):
        b = map(lambda x: 1 if x else 0, a)
        return reduce(lambda x, y: x + y, b, 0) / len(a)

    spell_checker = enchant.Dict(lang)
    words = [w.strip(string.punctuation + " ") for w in sentence.split(" ")]

    # Spell check every word and take a True ratio
    return _truth_ratio([(spell_checker.check(i.lower()) if i else False) for i in words]) > 0.7


def crack_affine(cipher, alphabet):
    l = len(alphabet)
    a = Affine(alphabet)

    keys = []
    for i in range(l ** 2):
        if not a.check_key(i):
            continue
        msg = a.decrypt(cipher, i)
        if is_speach(msg):
            keys.append(i)

    return keys
