# -*- coding: utf-8 -*-
"""
UnitTest for Millipede
"""

import unittest
import millipede


class TestMillipedeSize(unittest.TestCase):
    "Test size parameter on millipede function"

    def test_negative(self):
        "Test with negative integer value"
        self.assertEqual(
            millipede.millipede(-1),
            "    ╚⊙ ⊙╝\n"
        )

    def test_positive(self):
        "Test with positive integer value"
        self.assertEqual(
            millipede.millipede(1),
            """    ╚⊙ ⊙╝\n"""
            """  ╚═(███)═╝\n"""
        )

    def test_zero(self):
        "Test with 0"
        self.assertEqual(
            millipede.millipede(0),
            "    ╚⊙ ⊙╝\n"
        )

    def test_padding(self):
        "Test padding on sufficient size"
        self.assertEqual(
            millipede.millipede(10),
            """    ╚⊙ ⊙╝\n"""
            """  ╚═(███)═╝\n"""
            """ ╚═(███)═╝\n"""
            """╚═(███)═╝\n"""
            """ ╚═(███)═╝\n"""
            """  ╚═(███)═╝\n"""
            """   ╚═(███)═╝\n"""
            """    ╚═(███)═╝\n"""
            """    ╚═(███)═╝\n"""
            """   ╚═(███)═╝\n"""
            """  ╚═(███)═╝\n"""
        )


class TestMillipedeComment(unittest.TestCase):
    "Test comment parameter on millipede function"

    def test_empty(self):
        "Test with empty comment"
        self.assertEqual(
            millipede.millipede(0, comment=""),
            "    ╚⊙ ⊙╝\n"
        )

    def test_coucou(self):
        "Test with comment `coucou'"
        self.assertEqual(
            millipede.millipede(0, comment="coucou"),
            "coucou\n\n    ╚⊙ ⊙╝\n"
        )


class TestMillipedeReverse(unittest.TestCase):
    "Test reverse parameter on millipede function"

    def test_reverse(self):
        "Test with reverse enabled"
        self.assertEqual(
            millipede.millipede(1, reverse=True),
            """  ╔═(███)═╗\n"""
            """    ╔⊙ ⊙╗\n"""
        )

    def test_reverse_comment(self):
        "Test a comment with reverse enabled"
        self.assertEqual(
            millipede.millipede(1, comment="coucou", reverse=True),
            """  ╔═(███)═╗\n"""
            """    ╔⊙ ⊙╗\n\n"""
            """coucou\n"""
        )
