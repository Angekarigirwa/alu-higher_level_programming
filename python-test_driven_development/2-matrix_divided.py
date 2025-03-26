#!/usr/bin/pyhthon3
"""unittest module"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    """test max"""

    def test_max(self):
        """test max function"""
        self.assertEqual(max_integer([2,1,3]), 3)
        self.assertEqual(max_integer([-3,-4,-1]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([3,4,1]), 4)
        self.assertEqual(max_integer([8,4,1,3]), 8)
