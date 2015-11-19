# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:49:15 2015

@author: a998473
"""

import unittest
from time import time
import RainWater


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = RainWater.Solution()
        self.startTime = time()

    def tearDown(self):
        t = time() - self.startTime
        print("{0}: {1:.5f} seconds".format(self.id(), t))

    def test_empty(self):
        self.sol.trap([])

    def test_simple1(self):
        input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.sol.trap(input), 6)

    def test_simple2(self):
        input = [4, 2, 3, 4, 3, 4, 1, 4, 3]
        self.assertEqual(self.sol.trap(input), 7)

    def test_simple3(self):
        input = [4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.assertEqual(self.sol.trap(input), 0)

    def test_simple4(self):
        input = [4, 3, 4, 0, 2, 1, 2]
        self.assertEqual(self.sol.trap(input), 4)

    def test_hard1(self):
        input = []
        for i in range(20000):
            input.append(i)
        self.assertEqual(self.sol.trap(input), 0)

    def test_hard2(self):
        input = []
        for i in range(20000):
            if i % 2 == 1:
                input.append(i)
            else:
                input.append(0)
        # water = int(round(n / 2 - 1, 0))**2
        self.assertEqual(self.sol.trap(input), 99980001)

if __name__ == '__main__':
    unittest.main()
