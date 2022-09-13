#!/usr/bin/env python
# encoding: utf-8

import unittest
import cyclomatic_complexity as cc


class TestResult(unittest.TestCase):
    def test_init(self):
        self.assertEqual(cc.Result(), {})
        self.assertEqual(cc.Result(a=1), {"a": 1})
        self.assertEqual(cc.Result(dict(b=2)), {"b": 2})

    def test_get_set(self):
        res = cc.Result()
        res.a.b = 2
        res["c"]["d"] = 3
        self.assertEqual(res.a["b"], 2)
        self.assertEqual(res["c"].d, 3)

    def test_total(self):
        res = cc.Result(type="directoy")
        res.files.l1.types = "directoy"
        res.files.l1.files.l20.cyclomatic_complexity = 1
        res.files.l1.files.l21.cyclomatic_complexity = 2
        self.assertEqual(res.cyclomatic_complexity, 3)
