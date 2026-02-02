#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_boundary_min(self):
                self.assertEqual(1, calc(1, 1)) # 最小値（正常）

        def test_boundary_max(self):
                self.assertEqual(998001, calc(999, 999)) # 最大値（正常）

        def test_out_of_range_min(self):
                self.assertEqual(-1, calc(0, 500)) # 範囲外：下限（異常）

        def test_out_of_range_max(self):
                self.assertEqual(-1, calc(1000, 500)) # 範囲外：上限（異常）

        def test_type_error_string(self):
                self.assertEqual(-1, calc("abc", 100)) # 型エラー：文字列（異常）
