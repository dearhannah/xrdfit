import unittest
import numpy as np
from PreCurve import clear, smooth, picky


class TestPreCurve(unittest.TestCase):
    def test_clear(self):
        """Make sure the size of data did not change."""
        self.assertAlmostEqual(
            len(clear(np.array([[1, 10], [2, 20], [3, 30]]))), 3)

    def test_smooth(self):
        """Make sure value errors are raised when necessary"""
        self.assertRaises(ValueError, smooth, np.array(
            [[1, 10], [2, 20], [3, 30]]))
