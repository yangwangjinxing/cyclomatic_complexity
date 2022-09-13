#!/usr/bin/env python
# encoding: utf-8

import unittest
import cyclomatic_complexity as cc


class TestMain(unittest.TestCase):
    def test_file(self):
        res = cc.analyze("tests/data/src1.c")
        self.assertEqual(res.cyclomatic_complexity, 14)

    def test_directory(self):
        res = cc.analyze("tests/data")
        self.assertEqual(len(res.files.data2.files["src2.py"].functions), 3)
        self.assertEqual(res.cyclomatic_complexity, 17)
